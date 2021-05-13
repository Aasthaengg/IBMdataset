N, M = map(int, input().split())
ans = [0] * (N+1)
for i in range(M):
  a, b = map(int, input().split())
  ans[a] += 1
  ans[b] += 1

print(*ans[1:], sep='\n')