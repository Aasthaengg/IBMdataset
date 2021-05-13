d, g = map(int, input().split())
src = [list(map(int, input().split())) for _ in range(d)]

ans = 10**10
for b in range(2**d):
  score = 0
  ac = 0
  for k in range(d):
    if b&(1<<k):
      p,c = src[k]
      score += c
      ac += p
      score += p*(k+1)*100
  if score >= g:
    ans = min(ans, ac)
    continue
  for k in range(d-1, -1, -1):
    if b&(1<<k)==0:
      p, c = src[k]
      if score +p*(k+1)*100 < g:
        score += p*(k+1)*100
        ac += p
      else:
        rem = g-score
        ac += -(-rem // (k+1) // 100)
        ans = min(ans, ac)
        break
print(ans)