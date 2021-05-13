n,k = map(int,input().split())
a = list(map(int,input().split()))
dp = ['Second'] * (k+1)
for i in range(1,k+1):
    for j in range(1,n+1):
        if i-a[j-1] >= 0 and dp[i-a[j-1]] == 'Second':
            dp[i] = 'First'
print(dp[k])