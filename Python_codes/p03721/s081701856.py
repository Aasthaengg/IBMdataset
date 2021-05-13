N, K = map(int, input().split())
A = [0 for i in range(100001)]
for i in range(N):
  a, b = map(int, input().split())
  A[a] += b
for i in range(100001):
  if A[i] < K:
    K -= A[i]
  else:
    print(i)
    break