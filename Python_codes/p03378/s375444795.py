n,m,x=map(int,input().split())
a=list(map(int,input().split()))

ans=sum([a[i]>x for i in range(m)])
ans=min(ans,m-ans)
print(ans)