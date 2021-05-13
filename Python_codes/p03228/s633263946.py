A, B, K = map(int, input().split())
for i in range(K):
  if i % 2 == 0:
    A, B = A//2, A//2+B
  else:
    A, B = A+B//2, B//2
print(A,B)