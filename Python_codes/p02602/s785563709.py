N, K = map(int, input().split())
A = list(map(int, input().split()))
l = A[0]
r = A[K]
for i in range(1,N-K):
  if l < r:
    print('Yes')
  else:
    print('No')
  l = A[i]
  r = A[K+i]
if l < r:
  print('Yes')
else:
  print('No')