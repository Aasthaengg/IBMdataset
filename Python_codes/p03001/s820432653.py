w, h, x, y = map(int, input().split())
s = w * h / 2
if x == w / 2 and y == h / 2:
  print("{} {}".format(s, 1))
else:
  print("{} {}".format(s, 0))