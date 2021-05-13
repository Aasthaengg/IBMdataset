A, B, K = map(int,input().split())
for i in range(K):
  A2, B2 = A, B
  if i % 2 == 0:
    if A2 % 2 == 1: A2 -= 1
    B2 += A2 // 2
    A2 = A2 // 2
  else:
    if B2 % 2 == 1: B2 -= 1
    A2 += B2 // 2
    B2 = B2 // 2
  A, B = A2, B2
print(A, B)