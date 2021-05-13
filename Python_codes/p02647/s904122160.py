n,k = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    imos=[0]*(n+1)
    for i in range(n):
        mnind=max(0,i - a[i])
        mxind=min(n,i+ a[i]+1)
        imos[mnind]+=1
        imos[mxind]-=1
    for i in range(len(imos)-1):
        imos[i+1]+=imos[i]
    return imos[:n]

if k>50:
    k=50
for i in range(k):
    a = solve()
print(*a,sep=" ")