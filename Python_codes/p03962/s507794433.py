a, b, c = input().split()
colors = 0
if a == b and b == c:
  colors = 1
elif a == b or b == c or c == a:
  colors = 2
else:
  colors = 3
print(colors)