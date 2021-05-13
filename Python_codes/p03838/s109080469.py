x, y = map(int, input().split())
ans = 0
if x*y > 0:
  if x > y:
    ans = abs(x-y)+2
  else:
    ans = abs(x-y)
elif x*y < 0:
  ans = abs(abs(x)-abs(y))+1
else:
  if x == 0:
    if y < 0:
      ans = abs(x-y)+1
    else:
      ans = abs(x-y)
  else:
    if x < 0:
      ans = abs(x-y)
    else:
      ans = abs(x-y)+1
print(ans)