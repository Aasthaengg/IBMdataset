N, K = map(int, input().split())
if K % 2 == 1:
  p = N // K
  p *= p * p
  print(p)
else:
  p = N // K
  p *= p * p
  q = (N - K // 2) // K + 1
  q *= q * q
  print(p + q)