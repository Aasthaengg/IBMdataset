E = [set() for i in range(4)]
for i in range(3):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  E[a].add(b)
  E[b].add(a)
ok = True
for i in range(4):
  if len(E[i]) >= 3:
    ok = False
    break
if ok:
  print("YES")
else:
  print("NO")
