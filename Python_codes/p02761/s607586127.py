import sys

n, m = map(int, input().split())

conds = []
for _ in range(m):
  conds.append((input().split()))

for x in range(10 ** 3):
  xs = str(x)
  if len(xs) < n:
    continue

  found = True
  for cond in conds:
    s = int(cond[0]) - 1
    c = cond[1]
    if s >= len(xs):
      found = False
      break

    if xs[s] != c:
      found = False
      break

  if found:
    print(x)
    sys.exit()

print('-1')
