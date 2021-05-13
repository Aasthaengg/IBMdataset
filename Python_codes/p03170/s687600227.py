n,k=map(int,input().split())
A=list(map(int,input().split()))
dp=[False] * (k+1)
for i in range(k):
    for j in range(n):
        if dp[i]==False and i+A[j]<=k:
            dp[i+A[j]]=True
print('First' if dp[k] else 'Second')