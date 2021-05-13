A, B, K = map(int, input().split())

N = B - A + 1
limit = int(N / 2)
if K > limit:
  for i in range(A, B + 1):
    print(i)
else:
  for i in range(K):
    print(A + i)
  for i in range(K):
    print(B - K + 1 + i)

