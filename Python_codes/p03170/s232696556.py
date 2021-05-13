n,k=map(int,input().split())
A=sorted(map(int,input().split()))
dp=[0]*(k+1)
dp[1]=0
for i in range(k):
    if dp[i]==0:
        for a in A:
            if i+a<=k:
                dp[i+a]=1
print("Second"if dp[k]==0 else"First")