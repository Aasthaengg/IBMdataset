a, b = input().split()
x, y = map(int, input().split())
c = input()
if a == c:
  print("{} {}".format(x-1, y))
elif b == c:
  print("{} {}".format(x, y-1))
else:
  print("{} {}".format(x, y))