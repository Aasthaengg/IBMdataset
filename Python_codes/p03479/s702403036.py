n,m=map(int,input().split())
ans=0
now=n
while now<=m:
    ans+=1
    now*=2
print(ans)