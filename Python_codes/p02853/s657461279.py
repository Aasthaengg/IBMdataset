X,Y=map(int,input().split())
ans=0
ans+=max(0,400000-100000*X);
ans+=max(0,400000-100000*Y);
if X==1 and Y==1:
  ans+=400000
print(ans)
