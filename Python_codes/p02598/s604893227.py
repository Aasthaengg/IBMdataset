import math

def is_ok(A, x, K):
  cut_count = 0
  for number in A:
    cut_count += (math.ceil(number / x)) - 1
  return cut_count <= K

A = []
[N, K] = input().split()
N = int(N)
K = int(K)
A = input().split()
ans = 0

l = 0
r = 10 ** 9

for i in range(N):
  A[i] = int(A[i])

while r - l > 1:
  x = (r + l) // 2
  if is_ok(A, x, K):
    r = x
  else:
    l = x
      
print(r)