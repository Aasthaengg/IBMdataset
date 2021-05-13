N, M = map(int, input().split())
A = list(map(int, input().split()))
A = A[1:]
for i in range(N-1):
  B = list(map(int, input().split()))
  B = B[1:]
  A = set(A) & set(B)
ans = len(A)
print(ans)