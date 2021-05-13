W, a, b = map(int, input().split())
if min(a,b)+W >= max(a,b):
  print(0)
elif min(a,b)+W < max(a,b):
  print(max(a,b)-(min(a,b)+W))
