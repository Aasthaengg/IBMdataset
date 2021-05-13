K, S = map(int, input().split())

ans = 0
for i in range(K+1):
  mod = S - i
  if mod-K <= K:
    up = min(i+K+1, S+1)
    down = max(i, S-K)
    if up > down:
      plus = up - down
      ans += plus
print(ans)