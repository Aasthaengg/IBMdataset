import itertools

n,c=map(int,input().split())
dp=[[0]*100002 for i in range(c)]

for i in range(n):
    s,t,x=map(int,input().split())
    dp[x-1][s-1]+=1
    dp[x-1][t]-=1

for i in range(c):
    dp[i]=list(itertools.accumulate(dp[i]))


ans=0

for i in range(100001):
    cnt=0
    for j in range(c):
        if dp[j][i]!=0:
            cnt+=1
    
    ans=max(ans,cnt)


print(ans)