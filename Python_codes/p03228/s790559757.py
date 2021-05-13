A, B, K = map(int, input().split(' '))

for i in range(K):
  if i % 2 == 0:
    a = b = 0
    if A % 2 == 1:
      A -= 1
    a = A // 2
    A -= a
    B += a

  else:
    if B % 2 == 1:
      B -= 1
    b = B // 2
    B -= b
    A += b

print(A, B)
