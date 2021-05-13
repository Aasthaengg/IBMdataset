D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]

comp = [pc[i][0]*(i+1)*100+pc[i][1] for i in range(D)]

ans = 1000
for bit in range(2**D):
  solved = []
  for j in range(D):
    if 1&(bit>>j):
      solved.append(j)
  now = 0
  ps = 0
  for i in solved:
    now += comp[i]
    ps += pc[i][0]
  if now >= G:
    ans = min(ans, ps)
  else:
    for k in range(D):
      if D-k-1 in solved:
        continue
      if now + (D-k)*100*(pc[k][0]-1) >= G:
        ps += (G-now-100)//((D-k)*100) + 1
        ans = min(ans, ps)
      else:
        break
        
print(ans)
