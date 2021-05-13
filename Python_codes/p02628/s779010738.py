N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
min = 0

for i in range(K):
  min += A[i]
  
print(min)
