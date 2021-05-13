N,K = map(int,input().split())
A = list(map(int,input().split()))
max = 0
for i in range(K-1):
  value = A[i+1] - A[i]
  if max < value:
    max = value
value = (N - A[K-1]) + A[0]
if max < value:
  max = value
print(N - max)

