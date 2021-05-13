x,y = map(int,input().split())

if x==0:
  if y==0:
    ans=0
  elif y>0:
    ans = y
  else:
    ans = (-1)*y +1
elif y==0:
  if x==0:
    ans=0
  elif x>0:
    ans = 1+x
  else:
    ans = (-1)*x
else:
  if x>0 and y>0:
    if y>=x:
      ans=y-x
    else:
      ans= 1 + (x-y) +1
  elif x>0 and y<0:
    if x<(-1)*y:
      ans= (-1)*y-x +1
    else:
      ans= 1+(x+y)
  elif x<0 and y>0:
    if x<(-1)*y:
      ans=(-1)*y-x+1
    else:
      ans=1+ (x+y)
  else:
    if x<y:
      ans = y-x
    else:
      ans = 1 + ( (-1)*y+x) +1

print(ans)