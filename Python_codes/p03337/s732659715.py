a,b=map(int,input().split())
ans=max(a+b,a-b)
print(max(ans,a*b))
