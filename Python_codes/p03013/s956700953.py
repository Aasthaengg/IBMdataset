N,M = map(int, input().split())
A = [int(input()) for i in range(M)]
dp = [0]*(N+1)
for k in A:
    dp[k]="E"
dp[0]=1
if dp[1]=="E":
    dp[1]= 0
else:
    dp[1]= 1
for i in range(2,N+1):
    if dp[i]=="E":
        dp[i] = 0
    else:
        dp[i] = (dp[i-1]+dp[i-2])%(10**9+7)
print(dp[-1])