x, y = map(int, raw_input().split())
while True:
  z = x % y
  if z == 0:
    print y
    break
  x = y
  y = z