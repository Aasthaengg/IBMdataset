A, B, K = map(int, input().split())
for i in range(1, K+1):
  if(i%2==1):
    if(A%2 == 1):
      A = A-1
    B += A//2
    A = A//2
  else:
    if(B%2 == 1):
      B = B-1
    A += B//2
    B = B//2
print(A, B)