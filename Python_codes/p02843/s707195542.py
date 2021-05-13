n=int(input())
dp=[0]*(n+120)
dp[100]=1
dp[101]=1
dp[102]=1
dp[103]=1
dp[104]=1
dp[105]=1

for i in range(100,n+1):
    if not dp[i]: continue
    dp[i+100:i+106]= [1]*6
print(dp[n])
