A, B, C, K = map(int, input().split())
ans = A
if A > K:
  ans = K
if A + B < K:
  ans = A - (K-(A+B))
print(ans)