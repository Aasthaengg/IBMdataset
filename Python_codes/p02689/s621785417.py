N, M = map(int, input().split())
H = [0]+[int(h) for h in input().split()]
AB=[[] for n in range(N+1)]
for a, b in [[int(x) for x in input().split()] for m in range(M)]:
  AB[a].append(b)
  AB[b].append(a)
#print(AB)

ans=0
for i, ab in enumerate(AB):
  # rule2
  if not len(ab):
    ans+=0
  
  # rule1
  for j in ab:
    if H[i]<=H[j]:
      break
  else:
    ans+=1

print(ans-1) # decrease Observatroy index 0
