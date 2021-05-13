def solve():
  x, y = map(int, input().split())
  if y==0:
    return abs(x)+(x>0)
  if x==0:
    return abs(y)+(y<0)
  if y<x and x<0:
    return abs(abs(y)-abs(x))+2
  if x>y and y>0:
    return abs(abs(y)-abs(x))+2
  return abs(abs(y)-abs(x))+(x*y<0)
print(solve())