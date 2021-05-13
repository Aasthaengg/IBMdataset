N, M = map(int, input().split())
From = set()
To = set()
for _ in range(M):
  a, b = map(int, input().split())
  if a == 1:
    From.add(b)
  if b == N:
    To.add(a)
if From.isdisjoint(To):
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")