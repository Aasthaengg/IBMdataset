from itertools import product
from copy import deepcopy

n = int(input())
mod = 10 ** 9 + 7

comp = {"A": 0, "C": 1, "G": 2, "T": 3}
keys = comp.keys()

dp = [[0] * (4 ** 3) for _ in range(n + 1)]

bad = [0b001001, 0b000110, 0b100001]
for i in range(4 ** 3):
    if not i in bad:
        dp[3][i] = 1


def is_ok(li):
    for i in range(4):
        tmp = deepcopy(li)
        if i >= 1:
            tmp[i-1], tmp[i] = tmp[i], tmp[i-1]

        if "".join(tmp).count("AGC") >= 1:
            return False

    return True


def comp2int(li):
    ret = 0
    for i, e in enumerate(li):
        ret += comp[e] << 2 * (2 - i)

    return ret


for i in range(3, n):
    for last4 in product(keys, repeat=4):
        last4 = list(last4)
        if is_ok(last4):
            j_prev = comp2int(last4[:-1])
            j_nxt = comp2int(last4[1:])
            dp[i+1][j_nxt] += dp[i][j_prev]
            dp[i+1][j_nxt] %= mod

ans = 0
for i in range(4 ** 3):
    ans += dp[n][i]
    ans %= mod

print(ans)
