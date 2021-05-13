N, M = map(int, input().split())
S = []
for i in range(M):
  S.append(list(map(int, input().split())))
P = list(map(int, input().split()))
ans = 0
for n in range(2 ** N):
  t = [(n >> i) & 1 for i in range(N)]
  f = 0
  for j in range(M):
    c = 0
    for k in S[j][1:]:
      c ^= t[k-1]
    if c != P[j]:
      f = 1
      break
  if f == 0:
    ans += 1
print(ans)