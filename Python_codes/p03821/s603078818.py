N = int(input())
A = [None] * N
B = [None] * N
for i in range(N):
  A[i],B[i] = map(int, input().split())
  
ans = 0
for i in range(N):
  p = (A[N-1-i] + ans) % B[N-1-i]
  ans += (B[N-1-i] - p) % B[N-1-i]
print(ans)