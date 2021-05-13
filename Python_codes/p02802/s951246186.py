N, M = map(int, input().split())
WA = [0 for i in range(N+1)]
AC = [0 for i in range(N+1)]
for i in range(M):
  p, q = input().split()
  p = int(p)
  if q == "AC":
    AC[p] = 1
  else:
    if AC[p] == 0:
      WA[p] += 1
ans_WA = 0
for i, j in zip(WA, AC):
  ans_WA += i * j
print(sum(AC), ans_WA)