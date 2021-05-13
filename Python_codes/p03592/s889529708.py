N, M, K = map(int, input().split())

ans = 'No'
for k in range(N+1):
  for l in range(M+1):
    if k * (M - l) + l * (N - k) == K:
      ans = 'Yes'

print(ans)