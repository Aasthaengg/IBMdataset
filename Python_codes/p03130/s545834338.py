l = []
for i in range(3):
  a, b = map(int, input().split())
  l.append(a)
  l.append(b)
if sorted(l) == [1, 2, 2, 3, 3, 4]:
  print("YES")
else:
  print("NO")