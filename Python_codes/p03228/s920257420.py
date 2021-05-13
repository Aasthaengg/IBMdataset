A, B, K = map(int, input().split())
for i in range(K):
  if i%2==0:
    if A%2==1:
      A = A-1
    A //= 2
    B += A
  elif i%2==1:
    if B%2==1:
      B = B-1
    B //= 2
    A += B
print(A, B)