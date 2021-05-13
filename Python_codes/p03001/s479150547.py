w, h, x, y = map(int, input().split())
a = w * h / 2
if x * 2 == w and y * 2 == h:
  b = '1'
else:
  b = '0'
print(str(a) + ' ' + b)