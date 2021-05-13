N, T = list(map(lambda x : int(x), input().split(" ")))
cand = []
for i in range(N):
  c, t = list(map(lambda y : int(y), input().split(" ")))
  if t <= T:
    cand.append(c)

if len(cand) > 0:
  print(min(cand))
else:
  print("TLE")