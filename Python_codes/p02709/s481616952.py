import sys
from pprint import pprint
readline = sys.stdin.readline

N = int(readline())
A = list(map(int, readline().split()))

inds = [v[1] for v in sorted([(a, i) for i, a in enumerate(A)], reverse=True)]

dp = [[0] * (N+1) for i in range(N+1)]
dp[0][0] = 0

for y in range(N + 1):
    for x in range(N - y + 1):
        if x == 0 and y == 0:
            continue
        
        t = inds[x + y - 1]
        if y == 0:
            dp[y][x] = dp[y][x - 1] + A[t] * (t - (x - 1))
        elif x == 0:
            dp[y][x] = dp[y - 1][x] + A[t] * ((N - y) - t)
        else:
            dp[y][x] = max(dp[y][x - 1] + A[t] * (t - (x - 1)),
                dp[y - 1][x] + A[t] * ((N - y) - t))

ans = max([dp[i][N - i] for i in range(N + 1)])

print(ans)