K, S = list(map(lambda n: int(n), input().split(" ")))
cnt = 0
# X + Y + Z = S, 0 <= X, Y, Z <= K #
for x in range(K + 1):
  if S - x > 2 * K:
    continue
  for y in range(K + 1):
    if 0 <= S - x - y <= K:
      cnt += 1

print(cnt)
