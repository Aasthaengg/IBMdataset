h,w=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(10)]
dp=[0]*10
for i in range(10):
    dp[i]+=c[i][1]
for _ in range(11):
    for j in range(10):
        for k in range(10):
            dp[j]=min(dp[j],dp[k]+c[j][k])
count=0
for _ in range(h):
    a=list(map(int,input().split()))
    for l in a:
        if l!=-1:
            count+=dp[l]
print(count)
