x, y = sorted(list(map(int, input().split())), reverse=True)
while 1:
  if x % y == 0:
    print(y)
    break
  else:
    a = y
    b = x % y
    x = a
    y = b
