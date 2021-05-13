n,m=map(int,input().split())
ans=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        ans[b]+=1
    if b==n:
        ans[a]+=1

bl=False
for i in range(n):
    if ans[i]>=2:
        bl=True

if bl:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")