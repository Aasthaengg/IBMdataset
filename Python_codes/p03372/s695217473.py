import sys
from itertools import accumulate

def main():
  input = sys.stdin.readline
  N, C = map(int, input().split())
  X = []
  V = []
  for _ in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)
  Vr = V[::-1]
  Xr = X[::-1]

  F = list(accumulate(V))
  R = list(accumulate(Vr))
  F[0], R[0] = F[0] - X[0], R[0] - (C - Xr[0])
  for i in range(1, N):
    F[i] = max(F[i-1], F[i] - X[i])
    R[i] = max(R[i-1], R[i] - (C - Xr[i]))

  val = 0
  for i in range(N-1):
    v1 = F[i] + R[N-(i+2)] - X[i]
    v2 = R[i] + F[N-(i+2)] - (C - Xr[i])
    val = max(val, v1, v2)
  
  ans = max(0, val, max(F), max(R))
  print(ans)


if __name__ == '__main__':
  main()