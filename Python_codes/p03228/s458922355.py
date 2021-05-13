A,B,K = map(int,input().split())
c = 0
if K%2 == 0:
  while c < K:
    B = B+A//2
    A = A//2
    c += 1
    A = A+B//2
    B = B//2
    c += 1
else:
  while c < K-1:
    B = B+A//2
    A = A//2
    c += 1
    A = A+B//2
    B = B//2
    c += 1
  B = B+A//2
  A = A//2
print(A,B)