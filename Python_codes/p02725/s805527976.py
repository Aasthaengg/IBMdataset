k,n = list(map(int,input().split()))
A = list(map(int,input().split()))

max_distance = 0

for i in range(n):
  if max_distance < abs(A[i] - A[i-1]):
    max_distance = min(abs(A[i] - A[i-1]),k - abs(A[i] - A[i-1]))

print(k - max_distance)