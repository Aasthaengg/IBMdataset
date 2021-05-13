N=int(input())

lis=[]

temp=6
while temp<=N:
    lis.append(temp)
    temp*=6

temp=9
while temp<=N:
    lis.append(temp)
    temp*=9

lis.sort(reverse=True)

dp=[10**9]*(N+1)
dp[0]=0

#配列dp[N+1]にインデックスの数字を作るための最小手数をメモっていく
for item in lis:
    for i in range(N+1):
        if dp[i]!=10**9:
            if i+item<=N:
                dp[i+item]=min(dp[i]+1,dp[i+item])

ans=10**10
for index,item in enumerate(dp):
    ans=min(ans,item+N-index)
print(ans)