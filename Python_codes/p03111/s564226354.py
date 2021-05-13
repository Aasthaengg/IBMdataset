N, A, B, C = map(int, input().split())
X = [0, A, B, C]
L = [int(input()) for _ in range(N)]
d = 4 ** N
magic = int(1e+9)
for i in range(d):
  F = [0 for _ in range(4)]
  cnt = [0 for _ in range(4)]
  tmp = i
  for j in range(N):
    F[i%4] += L[j]
    cnt[i%4] += 1
    i //= 4
  p = True
  for k in range(1, 4):
    if F[k] == 0:
      p = False
      break
  tmpp = 0
  if p:
    for k in range(1, 4):
      tmpp += cnt[k] * 10 + abs(X[k] - F[k]) - 10
    if tmpp < magic:
      magic = tmpp
print(magic)