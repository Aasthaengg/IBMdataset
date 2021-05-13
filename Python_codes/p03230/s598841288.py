import sys
input = sys.stdin.readline
N = int(input())
f = 0
if N == 1:
  print("Yes")
  print(2)
  print(1, 1)
  print(1, 1)
  exit(0)
for i in range(1, N + 1):
  if i * (i + 1) == 2 * N:
    f = i + 1
    break
if f:
  print("Yes")
  print(f)
  res = [set() for _ in range(f + 1)]
  table = [0] * (N + 1)
  for i in range(N):
    res[i % f + 1].add(i + 1)
    table[i + 1] = 1
  for i in range(1, f + 1):
    for j in range(f - len(res[i]) - 1):
      for k in res[(i + j) % f + 1]:
        if table[k] < 2:
          res[i].add(k)
          table[k] += 1
          break
    print(len(res[i]), *sorted(res[i]))
else:
  print("No")
