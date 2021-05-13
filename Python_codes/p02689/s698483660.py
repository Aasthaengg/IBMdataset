n,m=map(int,input().split())
h=list(map(int,input().split()))

f=[1]*n
a=0
b=0

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if h[a]<=h[b]:
        f[a]=0
    if h[a]>=h[b]:
        f[b]=0

ans=0

for i in f:
    ans+=i

print(ans)