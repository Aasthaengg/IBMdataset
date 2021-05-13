n, a, b = map(int, input().split())
print(min(a,b), end=" ")
c = a+b-n
if 0 < c:
  print(c)
else:
  print(0)