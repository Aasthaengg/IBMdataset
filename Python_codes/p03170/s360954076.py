n,k=map(int,input().split())
a=list(map(int,input().split()))

dp=[0]*(k+1)

for i in range(1,k+1):
    x=1
    for j in range(n):
        if i-a[j]>=0:
            x *= dp[i-a[j]]
    if x==1:
        dp[i]=0
    else:
        dp[i]=1
if dp[k]==1:
    print("First")
else:
    print("Second")