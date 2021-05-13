n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(k+1)
dp[0]=0

for i in range(1,k+1):
    z=0
    for j in range(n):
        if i-a[j]>=0:
            if z==0:
                dp[i]=1
            dp[i]= dp[i] and dp[i-a[j]]
            z=1
    if z:
        dp[i]=(dp[i]+1)%2

print("First" if dp[k] else "Second")