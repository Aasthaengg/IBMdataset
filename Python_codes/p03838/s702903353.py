x,y = map(int,input().split())
k = abs(abs(x)-abs(y))
if x < 0 and y <= 0 or x >= 0 and y > 0:
  if x > y:
    k += 2
else:
  k += 1
print(k)
