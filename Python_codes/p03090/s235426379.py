import sys
input = sys.stdin.readline
N = int(input())
t = []
res = set()
for i in range(1, N // 2 + 1):
  if N % 2:
    t.append((i, N - i))
  else: t.append((i, N - i + 1))
for i in range(1, N):
  for x in t:
    if i in x: continue
    res.add(tuple(sorted((i, x[0]))))
    res.add(tuple(sorted((i, x[1]))))
if N % 2:
  for i in range(1, N):
    res.add((i, N))
print(len(res))
for r in res:
  print(*r)