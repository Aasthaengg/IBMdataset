N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]

D = [0] * N

for a, b in ab:
  a -= 1
  b -= 1
  D[a] += 1
  D[b] += 1

ans = True
for x in D:
  if x % 2 == 1:
    ans = False

if ans:
  print("YES")
else:
  print("NO")