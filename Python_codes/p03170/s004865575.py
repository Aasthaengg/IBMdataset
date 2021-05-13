n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[False]*(k+1)
for i in range(1,k+1):
    ok=False
    for j in range(n):
        if i-a[j]>=0:
            if not dp[i-a[j]]:
                ok=True
    if ok:
        dp[i]=True
if dp[k]:
    print("First")
else:
    print("Second")