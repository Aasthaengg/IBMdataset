a, b, c = map(int, input().split())

h = (a + b + c) // 2
A = (a + b + c) % 2

if A != 0:
  print("No")
  exit()

if h == a or h == b or h == c:
  print("Yes")
else:
  print("No")