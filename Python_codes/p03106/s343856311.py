A, B, K = map(int, input().split())
n = min(A, B)
while K:
  if A % n == 0 and B % n == 0:
    K -= 1
  if K == 0:
    print(n)
  n -= 1