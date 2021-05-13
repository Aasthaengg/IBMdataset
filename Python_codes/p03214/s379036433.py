N = int(input())
A = list(map(int, input().split()))
m = sum(A)
ans = 0
for i in range(N):
  if abs(A[i]*N - m) < abs(A[ans]*N - m):
    ans = i    
print(ans)
