n = int(input())
A = list(map(int, input().split()))
A.sort()

# 累積和取る。
for i in range(1, n):
  A[i] += A[i - 1]

k = 0
for i in range(0, n-1):
  if A[i] * 2 < A[i+1] - A[i]:
    k = i + 1
print(n-k)