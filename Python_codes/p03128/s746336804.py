n,m=map(int,input().split())
a=list(map(int,input().split()))
mm=[0,2,5,5,4,5,6,3,7,6]

dp=[0]
m = [mm[i] for i in range(10) if i in a]
for i in range(1,n+1):
    tres=[-10**10]
    for sm in m:
        if i - sm >= 0:
            tres.append(dp[i-sm]+1)
    dp.append(max(tres))
k=dp[n]
res = []
a.sort(reverse=True)
while n > 0:
    for sa in a:
        if n-mm[sa] >= 0 and dp[n-mm[sa]]==dp[n]-1:
            res.append(sa)
            n -= mm[sa]
            break

print("".join(map(str,res)))