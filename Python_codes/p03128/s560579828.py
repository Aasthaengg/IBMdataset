N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
c = [0,2,5,5,4,5,6,3,7,6]

dp = [-1]*(N+1)
dp[0] = ''
for a in A:
    if c[a] <= N:
        dp[c[a]] = str(a)

for i in range(N+1):
    for a in A:
        if i-c[a]>=0 and dp[i-c[a]]!=-1:
            if dp[i]==-1 or len(dp[i]) <= len(dp[i-c[a]])+1:
                dp[i] = str(a)+dp[i-c[a]]

ans = sorted(dp[N])
ans = ans[::-1]
ans = ''.join(ans)
print(ans)