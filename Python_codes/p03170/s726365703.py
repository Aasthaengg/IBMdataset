n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
dp = [0 for i in range(k+1)]
dp[0]=2
for i in range(1,k+1):
    l=0
    for j in range(n):
        if dp[i-a[j]]==2:
            l=l+1
            break
    if l==1:
        dp[i]=1
    else:
        dp[i]=2
if dp[k]==1:
    print("First")
else:
    print("Second")
