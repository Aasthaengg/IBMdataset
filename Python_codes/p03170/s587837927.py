n,k=map(int,input().split())
arr=[int(i) for i in input().split()]
dp=[0 for i in range(k+1)]
for i in range(1,k+1):
    for j in range(n):
        if arr[j]<=i and dp[i-arr[j]]==0:
            dp[i]=1
if dp[k]==1:
    print("First")
else:
    print("Second")
