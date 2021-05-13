a,b,c=map(int,input().split())
d=a+b+c
m=max(a,b,c)
if d%2==0:
  if m%2==0:
    m=m
  else:
    m=m+1
else:
  if m%2==0:
    m=m+1
  else:
    m=m
s=3*m
ans=s-d
ans//=2
print(ans)