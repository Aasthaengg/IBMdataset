import bisect

N,C = map(int,input().split())
STC = [list(map(int,input().split())) for _ in range(N)]
STC.sort(key=lambda x:x[1])
#print(STC)

P = {}
for p in STC:
  if p[2] not in P:
    P[p[2]] = [p[:2]]
  else:
    pe = P[p[2]][-1]
    if pe[1] == p[0]:
      P[p[2]][-1][1] = p[1]
    else:
      P[p[2]].append(p[:2])
#print(P)

P2 = []
maxt = 0
for val in P.values():
  for v in val:
    P2.append([v[0]-1,v[1]])
    maxt = max(maxt,v[1])
#print(P2)

T = [0 for _ in range(maxt+2)]
for p in P2:
  T[p[0]] += 1
  T[p[1]] -= 1
#print(T)
for i in range(1,maxt+2):
  T[i] += T[i-1]
#print(T)
print(max(T))
