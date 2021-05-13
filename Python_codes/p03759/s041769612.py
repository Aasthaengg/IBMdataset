a, b, c = map(int, input().split())
x = b - a
y = c - b
if x == y:
  print("YES")
else:
  print("NO")