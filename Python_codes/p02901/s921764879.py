# import sys
# sys.setrecursionlimit
getarr = lambda _f: list(map(_f, input().split()))
inf = 10**8 + 1

N, M = getarr(int)

keys = []
key_max = 2**N - 1
for _ in range(M):
    a, b = getarr(int)
    c = getarr(int)
    k = key_max
    for ci in c:
        k -= (1 << (ci - 1))
    keys.append([a, k])
dp = [[inf] * (M + 1) for _ in range(2**N + 1)]
for i in range(M + 1):
    dp[0][i] = 0

for j in range(M):
    for i in range(2**N + 1):
        _cost = keys[j][0]
        _key = keys[j][1]
        dp[i][j + 1] = min(_cost + dp[i & _key][j], dp[i][j])

ans = dp[key_max][M]

print(ans if ans != inf else -1)