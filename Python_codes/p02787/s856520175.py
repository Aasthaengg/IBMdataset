a=[]
dp=[float("inf") for i in range(1+10**4)]
h,n=map(int,input().split())
for i in range(n):
    A,B=map(int,input().split())
    a.append((A,B))
dp[0]=0
for i in range(1+10**4):
    for A,B in a:
        dp[i]=min(dp[i],dp[max(0,i-A)]+B)
print(dp[h])