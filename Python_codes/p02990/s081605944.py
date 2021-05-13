import sys
import numpy as np

MOD = 10 ** 9 + 7


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


def comb(n, r, facts, invs, MOD):
    return facts[n] * invs[r] * invs[n - r] % MOD


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    facts, invs = prepare(2100, MOD)
    for i in range(1, k + 1):
        if n - k < i - 1:
            print(0)
        else:
            print(
                comb(n - k + 1, i, facts, invs, MOD)
                * comb(k - 1, i - 1, facts, invs, MOD)
                % MOD
            )


if __name__ == "__main__":
    main()
