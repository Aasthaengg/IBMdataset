def solve():
  t = [[] for _ in range(4)]
  for _ in range(3):
    a, b = map(int, input().split())
    if b-1 in t[a-1]:
      print("NO")
      return
    if a-1 in t[b-1]:
      print("NO")
      return
    t[a-1].append(b-1)
    t[b-1].append(a-1)

  for i in range(4):
    if len(t[i]) == 0:
      print("NO")
      return
    if len(t[i]) == 3:
      print("NO")
      return

  print("YES")
solve()