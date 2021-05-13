n,k = map(int, input().split())
A = list(map(int, input().split()))
counter = 0

for i in range(0,n,k-1):
  min_n = min(A[i:i+k])
  max_n = max(A[i:i+k])
  if min_n != max_n:
    counter += 1
  if i+k-1 < n:
    A[i+k-1] = min_n
  
print(counter)