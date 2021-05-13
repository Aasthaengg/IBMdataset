w,a,b=map(int,input().split())
d=max(a,b)
c=min(a,b)
if d-c<=w:
  ans=0
else:
  ans=d-c-w
print(ans) 