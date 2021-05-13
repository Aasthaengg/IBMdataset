N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if(A[0] > X):
  ans += (A[0]-X)
  A[0] = X
for i in range(1,N):
  S = A[i-1] + A[i]
  if(S > X):
    ans += S-X
    A[i] -= S-X
print(ans)