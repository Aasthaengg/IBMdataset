x,y = map(int,input().split())
n = abs(abs(x)-abs(y))
if x >=0:
  if y > 0:
    if y>x:
      ans = n
    else:
      ans = n+2
  else:
    ans = n+1
else:
  if y > 0:
    ans = n+1
  else:
    if y > x:
      ans = n
    else:
      ans = n+2
print(ans)