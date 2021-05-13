N=int(input())
X=list(map(int,input().split()))

dp=[0 for i in range(100)]
i=1
for j in range(N):
    dp[0]+=(X[j]-0)**2

while True:
    for j in range(N):
        dp[i]+=(X[j]-i)**2
    if dp[i]>=dp[i-1]:
        break
    i+=1

ans=dp[i-1]
print(ans)