N, M, P = list(map(int, input().split()))
ABC = [list(map(int, input().split())) for _ in range(M)]

class edge:
   f, t, c = 0, 0, 0

inf = 10 ** 5 * (M + 1)
D = [inf] * N
D[0] = 0
E = [edge() for _ in range(M)]
for i in range(M):
  f, t, c = ABC[i]
  E[i].f = f - 1
  E[i].t = t - 1
  E[i].c = P - c
  
L = [False] * N
L[-1] = True
for i in range(N):
  for j in range(M):
    e = E[j]
    if L[e.t]:
      L[e.f] = True

cnt = N + 1
while True:
  flag = True
  for i in range(M):
    e = E[i]
    if D[e.f] != inf and D[e.t] > D[e.f] + e.c:
      D[e.t] = D[e.f] + e.c
      flag = False
      if cnt == 1:
        if L[e.t]:
          print(-1)
          exit()
  if flag:
    break
  cnt -= 1
  if cnt <= 0:
    break

print(max(0, -D[-1]))