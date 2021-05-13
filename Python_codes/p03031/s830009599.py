N, M = map(int, input().split())
S = [tuple(map(int, input().split()))[1:] for _ in range(M)]
P = tuple(map(int, input().split()))

ans = 0
for state in range(2 ** N):
  for m in range(M):
    count = 0
    for s in S[m]:
      if state & (1 << (s - 1)):
        count += 1
    if count % 2 != P[m]:
      break
  else:
    ans += 1
print(ans)