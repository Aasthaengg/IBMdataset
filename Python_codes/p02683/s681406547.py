from sys import stdin,stdout
def fn(mask):
    global ans
    cost=0
    b=[0]*(1+m)
    for i in range(n):
        if mask&(1<<i):
            cost+=a[i][0]
            for j in range(1,m+1):
                b[j]+=a[i][j]
    allowed=all([v>=c for v in b[1:]])
    if allowed:ans=min(ans,cost)
n,m,c=list(map(int,stdin.readline().split()))
a=[list(map(int,stdin.readline().split())) for _ in range(n)]
ans=float('inf')
for mask in range(1<<n):
    fn(mask)
print(ans if ans!=float('inf') else -1)
