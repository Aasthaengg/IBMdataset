N,K=map(int,input().split())
a=list(map(int,input().split()))

dp=[False]*(K+1)

for i in range(N):
    dp[a[i]]=True

for k in range(K+1):
    for n in range(N):
        if k>=a[n]:
            dp[k]=not dp[k-a[n]]
        if dp[k] is True:
            break

if dp[-1] is True:
    print("First")
else:
    print("Second")