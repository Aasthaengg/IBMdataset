import sys;input=sys.stdin.readline
N, M = map(int, input().split())
inf = 10**18
dp = [inf]*(1<<N)
dp[0] = 0
for i in range(M):
    a, b = map(int, input().split())
    Cs = list(map(int, input().split()))
    bb = 0
    for c in Cs:
        bb += 2**(c-1)
    for x in range((1<<N)-1, -1, -1):
        dp[bb|x] = min(dp[x]+a, dp[bb|x])

#print(dp)
r = dp[(1<<N)-1]
if r != inf:
    print(dp[(1<<N)-1])
else:
    print(-1)
