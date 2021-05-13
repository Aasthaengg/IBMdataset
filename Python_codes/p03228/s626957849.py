data = list(map(int, input().split()))

def cookie1(a, b):
  if a % 2 == 1:
    a = a - 1
  else:
    pass
  return (int(a / 2), b + int(a / 2))

def cookie2(a, b):
  if b % 2 == 1:
    b = b - 1
  else:
    pass
  return (a + int(b / 2), int(b / 2))

a = data[0]
b = data[1]
for i in range(data[2]):
  if i % 2 == 0:
    c = cookie1(a, b)
    a = c[0]
    b = c[1]
  else:
    c = cookie2(a, b)
    a = c[0]
    b = c[1]
print("{0} {1}".format(a, b))