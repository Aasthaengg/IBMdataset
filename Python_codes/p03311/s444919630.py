N = int(input())
A = list(map(int, input().split()))
for i in range(N):
  A[i] -= i
A.sort()

n = (N-1) // 2
q = A[n]
ans = 0
for i in range(N):
  ans += abs(A[i]-q)
print(ans)