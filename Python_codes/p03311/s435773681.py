N = int(input())
A = list(map(int, input().split()))
for i in range(N):
  A[i] -= i
  
mode = sorted(A)[N//2]

ans = 0
for i in range(N):
  ans += abs(A[i]-mode)
print(ans)