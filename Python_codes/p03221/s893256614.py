from bisect import bisect_right

N, M = map(int, input().split())

Ps, Ys, vals = [], [], {}
for i in range(M):
  P, Y = map(int, input().split())
  Ps.append(P)
  Ys.append(Y)

  if P not in vals:
    vals[P] = []
  vals[P].append(Y)

for P in vals:
  vals[P].sort()

for i in range(M):
  pref = str(Ps[i]).zfill(6)
  city = str(bisect_right(vals[Ps[i]], Ys[i])).zfill(6)
  print(pref + city)
