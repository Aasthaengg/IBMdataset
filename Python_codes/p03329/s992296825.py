n=int(input())
lst=[1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]

dp=[None]*(n+1) #リストの番号と同じお金を払うのに必要な最短手数
dp[0]=0
for i in lst:
    if i<=n:
        dp[i]=1

for i in range(2,n+1):
    kouho=[]
    for j in lst:
        if i-j>=0:
            kouho.append(dp[i-j]+1)
    dp[i]=min(kouho)

print(dp[-1])