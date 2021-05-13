N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 1

for i in range(1, N):
  if A[i] > A[i - 1] * 2:
    ans = 1
  else:
    ans += 1
  A[i] += A[i - 1]

print(ans)