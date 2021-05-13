a,b,c,d=map(int,input().split())
ans=0
if a==2*c and b==2*d:
  ans=1
print(a*b/2,ans)