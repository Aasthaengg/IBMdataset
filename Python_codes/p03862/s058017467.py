import copy
n, x = map(int, input().split())
A = list(map(int, input().split()))
B = copy.deepcopy(A)

if A[0] > x:
  A[0] = x
for i in range(1, len(A)):
  if A[i-1] + A[i] > x:
    A[i] = x - A[i-1]
ans = 0
for a, b in zip(A, B):
  ans += b - a
print(ans)
