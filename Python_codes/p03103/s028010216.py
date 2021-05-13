N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
L.sort(key=lambda x: x[0])
S = 0
for l in L:
  if l[1]>=M:
    S += l[0]*M
    break
  else:
    S += l[0]*l[1]
    M -= l[1]
print(S)