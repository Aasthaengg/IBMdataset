N, M = list(map(int, input().split()))
ks = [list(map(int, input().split())) for _ in range(M)]
p = list(map(int, input().split()))

ans = 0
B = 1 << N
for i in range(B):
  L = [0] * M
  for j in range(M):
    for k in ks[j][1:]:
      if i >> (k - 1) & 1:
        L[j] = (L[j] + 1) % 2
  for j in range(M):
    if L[j] != p[j]:
      break
  else:
    ans += 1

print(ans)