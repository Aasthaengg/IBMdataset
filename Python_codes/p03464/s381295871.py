K = int(input())
A = list(map(int, input().split()))

def ng():
  print(-1)
  exit()

A = A[::-1]
if A[0] != 2:
  ng()
mim = 2
mox = 3

for i in range(1, K):
  a = A[i]
  n = -(-mim // a) * a
  if n > mox:
    ng()
  mim = n
  mox = mox // a * a + a - 1

print(mim, mox)