x, y = map(int, input().split())
a = 2000000000
if y >= x:
  a = y - x
if -y >= x:
  b = -x - y + 1
  if b < a:
    a = b
if y >= -x:
  b = x + y + 1
  if b < a:
    a = b
if -y >= -x:
  b = x - y + 2
  if b < a:
    a = b
print(a)