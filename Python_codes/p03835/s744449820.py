K, S = map(int, input().split())
ans = 0
for i in range(0, K+1):
  if i > S:
    break
  for j in range(0, K+1):
    if i + j > S:
      break
    if S - i - j <= K:
      ans += 1
print(ans)