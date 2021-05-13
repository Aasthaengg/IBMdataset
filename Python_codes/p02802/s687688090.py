N, M = map(int, input().split())
P = [input().split() for _ in range(M)]
 
wa = [0]*N
ac = [False]*N
 
for ps in P:
  p, s = int(ps[0]), ps[1]
  if ac[p-1]:
    continue
  elif s == 'AC':
    ac[p-1] = True
  else:
    wa[p-1] += 1

print(sum(ac), sum([w*a for w,a in zip(wa, ac)]))