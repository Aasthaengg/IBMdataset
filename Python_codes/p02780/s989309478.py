N, K = map(int,input().split())
p = list(map(int,input().split()))

li = [0] * N
for i in range(N): li[i] = sum(range(1, p[i]+1)) / p[i]

ans, total = sum(li[:K]), sum(li[:K])
if N != K:
  for i in range(1, N - K + 1):
    total = total - li[i-1] + li[i-1+K]
    ans = max(ans, total)
  print(ans)
else: print(ans)