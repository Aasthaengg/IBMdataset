D, G = list(map(int, input().split()))

p, c = [], []
for i in range(1,D+1):
  pi,ci = list(map(int, input().split()))
  p.append(pi)
  c.append(ci)

res = float('inf')

for i in range(2**D):
  score, solved = 0, 0
  all_solved = []

  for j in range(D):
    if (i>>j)&1:
      score += 100*(j+1)*p[j] + c[j]
      solved += p[j]
      all_solved.append(j)
      if score >= G: break

  if score < G:
    for k in range(D-1, -1, -1):
      if k not in all_solved:
        for num in range(p[k]):
          score += 100*(k+1)
          solved += 1
          if score >= G: break
        if score >= G: break
        score += c[k]

  if score >= G:
    res = min(res, solved)

print(res)