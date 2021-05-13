a, b = map(int, input().split())
x = max(a, b)
y = min(a, b)
if (x - y) % 2:
  print("IMPOSSIBLE")
else:
  print(y + int((x - y) / 2))
