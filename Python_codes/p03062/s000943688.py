N = int(input())
A = list(map(int, input().split()))
a = 0
for i in range(N):
  if A[i] < 0:
    a += 1
    A[i] *= -1
ans = sum(A)
if a % 2 == 1:
  A.sort()
  ans -= 2 * A[0]
print(ans)
  
