a, b, c = map(int, input().split())
d = b-a+1
if d < c*2+1:
  for i in range(d):
    print(a)
    a = a+1
else:
  b = b-c+1
  for i in range(c):
    print(a)
    a = a+1
  for i in range(c):
    print(b)
    b = b+1