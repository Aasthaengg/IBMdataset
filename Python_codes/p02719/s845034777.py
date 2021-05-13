N, K = map(int, input().split())
if N > K:
  N -= (N//K)*K
ans = N if N <= abs(N-K) else abs(N-K)
print(ans)

# flag = True
# while flag:
#   if N > K:
#     N = abs(N-K)
#   else:
#     ans = N if N <= N -K else N-K
#     flag = False