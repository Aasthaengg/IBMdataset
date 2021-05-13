from itertools import accumulate
n, k = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(k):
  B = [0]*(n+1)
  for i, a in enumerate(A):
    B[max(i-a, 0)] += 1
    B[min(i+a+1, n)] -= 1
  A = list(accumulate(B))[:-1]
  if min(A) == n:
    break
print(*A)