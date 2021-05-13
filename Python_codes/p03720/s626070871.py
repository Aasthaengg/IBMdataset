n, m = map(int, input().split())
ans = [0 for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  ans[a] += 1
  ans[b] += 1
print(*ans, sep = "\n")