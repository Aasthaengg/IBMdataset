N, M = map(int, input().split())
S = [list(map(int, input().split())) for i in range(N)]
S.sort()
ans = 0
k = M
for i in range(N):
  if k == 0:
    break
  elif S[i][1] <= k:
    k -= S[i][1]
    ans += S[i][0] * S[i][1]
  else:
    ans += S[i][0] * k
    k = 0
print(ans)