INF = float('inf')
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
c = [0,2,5,5,4,5,6,3,7,6]

dp = [-INF]*(N+1)
dp[0] = 0
for a in A:
    if c[a] <= N:
        dp[c[a]] = 1

for i in range(N+1):
    for a in A:
        if i-c[a]>=0:
            dp[i] = max(dp[i],dp[i-c[a]]+1)

ans = ''
n = N
for a in A:
    if n-c[a]>=0:
        while dp[n] == dp[n-c[a]]+1:
            n -= c[a]
            ans = ans + str(a)
print(ans)