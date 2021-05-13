import numpy as np
import sys
x, y = map(int, input().split())

if (x + y) % 3 != 0 or x > 2 * y or y > 2 * x:
    print(0)
    sys.exit()

# 手数
n = (x + y) // 3
x -= n
y -= n

MOD = 10**9 + 7


def prepare(n, MOD):
    nrt = int(n ** 0.5) + 1
    nsq = nrt * nrt
    facts = np.arange(nsq, dtype=np.int64).reshape(nrt, nrt)
    facts[0, 0] = 1
    for i in range(1, nrt):
        facts[:, i] = facts[:, i] * facts[:, i - 1] % MOD
    for i in range(1, nrt):
        facts[i] = facts[i] * facts[i - 1, -1] % MOD
    facts = facts.ravel().tolist()

    invs = np.arange(1, nsq + 1, dtype=np.int64).reshape(nrt, nrt)
    invs[-1, -1] = pow(facts[-1], MOD - 2, MOD)
    for i in range(nrt - 2, -1, -1):
        invs[:, i] = invs[:, i] * invs[:, i + 1] % MOD
    for i in range(nrt - 2, -1, -1):
        invs[i] = invs[i] * invs[i + 1, 0] % MOD
    invs = invs.ravel().tolist()

    return facts, invs


facts, invs = prepare(n, MOD)

print(facts[n] * invs[x] * invs[y] % MOD)