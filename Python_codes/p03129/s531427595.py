N, K = map(int, input().split())
ans = 0

for i in range(1, N+1):
  if i % 2 == 1:
    ans += 1

if ans >= K:
  print("YES")
else:
  print("NO")