N = int(input())
A = list(map(int,input().split()))
M = sum(A) / N
std = float("inf")
ans = 0
for i in range(N):
  if abs(M - A[i]) < std:
    std = abs(M - A[i])
    ans = i
print(ans)

