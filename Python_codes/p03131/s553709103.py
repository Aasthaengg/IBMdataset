K, A, B = map(int, input().split())
st = 1
hit = 0
if K <= A - 1:
  print(K + 1)
else:
  if B - A <= 1:
    print(K + 1)
  else:
    K -= A - 1
    print(A + (K // 2) * (B - A) + K % 2)