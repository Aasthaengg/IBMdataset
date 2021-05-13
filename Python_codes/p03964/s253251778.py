def ceil(a, b):
  return a // b + (a % b > 0)

N = int(input())
T = A = 1
for i in range(N):
  t, a = map(int, input().split())
  m = max(ceil(T, t), ceil(A, a))
  T = t * m
  A = a * m
print(T + A)