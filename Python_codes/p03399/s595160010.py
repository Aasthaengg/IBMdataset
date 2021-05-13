a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= b:
  if c <= d:
    print(a + c)
  else:
    print(a + d)
else:
  if c <= d:
    print(b + c)
  else:
    print(b + d)
