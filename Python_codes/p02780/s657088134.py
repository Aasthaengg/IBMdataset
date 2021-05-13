N, K = map(int, input().split())
p = list(map(int, input().split()))
prospect = []
for k in range(N):
  if p[k]%2 == 1:
    prospect.append((p[k]+1)>>1)
  else:
    prospect.append((p[k]+1)/2)
S = sum(prospect[:K])
ans = 0 + S
for k in range(N-K):
  S += prospect[k+K] - prospect[k]
  ans = max(ans, S)
print(ans) 