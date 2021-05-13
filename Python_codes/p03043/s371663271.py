N, K = map(int, input().split())

ans = 0
for point in range(1, N+1):
  cnt = 1/N
  while (point<K):
    cnt /= 2
    point *= 2
  ans += cnt
print(ans)