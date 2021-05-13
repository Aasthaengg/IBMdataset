x,y=[int(s) for s in input().split()]
ans=0
if x<4:
  ans+=100000
if x<3:
  ans+=100000
if x<2:
  ans+=100000
if y<4:
  ans+=100000
if y<3:
  ans+=100000
if y<2:
  ans+=100000
if x*y==1:
  ans+=400000
print(ans)
  
