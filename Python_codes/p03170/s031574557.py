n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(k+1)
for i in range(k+1):
    for j in range(n):
        if i-a[j]<0:
            break
        if not dp[i-a[j]]:
            dp[i]=1
            break
print('First' if dp[k] else 'Second')