K = int(input())
A = list(map(int, input().split()))
def ceiling(x, mod):
  if x % mod == 0:
    return x // mod
  else:
    return x // mod + 1

m, M = 2, 2
p = 0
for i in range(K-1, -1, -1):
  m, M = A[i] * ceiling(m, A[i]), A[i] * (M // A[i]) + A[i] - 1
chk1, chk2 = m, M
for i in range(K):
  chk1, chk2 = A[i] * (chk1 // A[i]), A[i] * (chk2 // A[i])
if chk1 == 2 and chk2 == 2:
  print(m, M)
else:
  print(-1)