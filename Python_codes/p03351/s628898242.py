a, b, c, d = map(int, input().split())
def check(x, y):
  return abs(x - y) <= d
if (check(a, c)) or (check(a, b) and check(b, c)):
  print("Yes")
else: print("No")