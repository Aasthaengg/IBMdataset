N, M = list(map(int, input().split()))
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
  for j in range(M):
    t = 0
    for k in range(1, ks[j][0] + 1):
      if i >> (ks[j][k] - 1) & 1:
        t += 1
    if t % 2 != p[j]:
      break
  else:
    ans += 1

print(ans)
