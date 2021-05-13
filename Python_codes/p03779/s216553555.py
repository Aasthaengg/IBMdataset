def calcTime(x):
  n = 0
  while True:
    if n*(n+1)//2 > x:
   	  return n
    elif n*(n+1)//2 == x:
      return n
    else:
      n += 1

x = int(input())
ans = calcTime(x)
print(ans)