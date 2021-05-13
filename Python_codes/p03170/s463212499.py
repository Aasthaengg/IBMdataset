n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[False]*(k+1)
for i in range(1,k+1):
    for j in a:
        if i-j<0:continue
        if dp[i-j]==False:dp[i]=True
if dp[k]:print("First")
else:print("Second")