N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
match = [0,2,5,5,4,5,6,3,7,6]
dp = [0]+[-1]*N

for i in A:
    for j in range(0,N+1):
        if j-match[i] >= 0:
            dp[j] = max(dp[j-match[i]]*10+i,dp[j])
print(dp[-1])
