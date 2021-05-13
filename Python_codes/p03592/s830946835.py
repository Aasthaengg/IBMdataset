N, M, K = map(int, input().split())
ans = "No"
for n in range(N+1):
  for m in range(M+1):
    if (N*m + M*n - 2*m*n) == K:
      ans = "Yes"
      break
print(ans)