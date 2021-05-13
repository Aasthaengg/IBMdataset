H, W = map(int, input().split())
N = int(input())
A = [int(x) for x in input().split()]
C = []
for i in range(N):
  C += [str(i + 1)] * A[i]
for j in range(H):
  out = C[:W]
  if j % 2:
    out.reverse()
  print(' '.join(out))
  C = C[W:]
