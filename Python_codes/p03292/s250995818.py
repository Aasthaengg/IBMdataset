A = list(map(int, input().split()))
A.sort()
sum = 0

for i in range(len(A)-1):
  sum += A[i + 1] - A[i]
print(sum)
