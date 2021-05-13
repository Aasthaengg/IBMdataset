N = int(input())
A = list(map(int, input().split()))
p = 1
n = A[0]
for i in range(1, N):
  p = n + p * A[i]
  n = n * A[i]
print(n / p)