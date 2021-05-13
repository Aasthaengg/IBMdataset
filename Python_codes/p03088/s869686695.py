from itertools import product
import sys
sys.setrecursionlimit(10**9)

N, MOD = int(input()), 10 ** 9 + 7
dp = [[0] * 64 for _ in range(N+1)]
strs = [""] * 64
strs_d = {}
for i, s in enumerate(product("AGCT", repeat=3)):
    strs[i] = "".join(s)
    strs_d["".join(s)] = i

def check(s):
    assert len(s) == 4
    if "".join(s).count("AGC") >= 1:
        return False
    for i in range(3):
        s[i], s[i + 1] = s[i + 1], s[i]
        if "".join(s).count("AGC") >= 1:
            return False
        s[i], s[i + 1] = s[i + 1], s[i]
    return True

# dp[i][str] := N-i桁かつ末尾4桁がstr文字列のとき、作成可能な文字列の個数

dp[0] = [1] * 64
for i in range(1,1+N):
    for j, s in enumerate(strs):
        for ns in "AGCT":
            if check(list(s+ns)):
                dp[i][strs_d[s[1:]+ns]] += dp[i-1][j]
                dp[i][strs_d[s[1:]+ns]] %= MOD

if N == 3:
    print("61")
else:
    print(sum(dp[N-3])%MOD)

