a,b,c=map(int,input().split())
ans=min(a+b,a+c)
ans=min(ans,b+c)
print(ans)
