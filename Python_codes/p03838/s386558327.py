x,y = map(int, input().split())
ans = 0

if (x==0 and y>0) or (y==0 and x<0):
  ans = abs(abs(y)-abs(x))
elif (x==0 and y<0) or (y==0 and x>0):
  ans = abs(abs(y)-abs(x))+1
else:
  ans = abs(abs(y)-abs(x))
  if x>0 and y>0:
    if x>y:
      ans += 2
  elif x>0 and y<0:
    ans += 1
  elif x<0 and y>0:
    ans += 1
  elif x<0 and y<0:
    if x>y:
      ans += 2

print(ans)


