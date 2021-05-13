K, T = map(int, input().split())
N = (K + 1) // 2
A = list(map(int, input().split()))
a = max(A)
if a <= N:
  print(0)
else:
  print(2 * (a - N) - 1)