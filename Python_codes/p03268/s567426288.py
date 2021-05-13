N, K = map(int, input().split())
cnt = pow(N // K, 3)
if K % 2 == 0:
  tmp = 0
  for i in range(1, N+1):
    if i % K == K / 2:
      tmp += 1
  cnt += pow(tmp, 3)
print(cnt)
