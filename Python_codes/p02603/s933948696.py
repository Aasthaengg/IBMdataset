n = int(input())
A = list(map(int, input().split()))

ret = 1000
for i in range(1, n):
  if A[i] - A[i - 1] > 0:
    ret = A[i] * (ret // A[i - 1]) + ret % A[i - 1]

print(ret)