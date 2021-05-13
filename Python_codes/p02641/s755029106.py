import math
X, N = list(map(lambda n : int(n), input().split(" ")))
if N == 0:
  print(X)
else:
  P = list(map(lambda p : int(p), input().split(" ")))
  Q = list(map(lambda p : [p, abs(X-p)], P))
  Q.sort(key=lambda q: (q[1], q[0]))

  cand = []
  for i in range(N):
    if i == 0 and Q[0][1] != 0:
      cand.append(X)
      break
    else:
      if Q[i][1] != math.ceil(i/2):
        cand.append(X + math.ceil(i/2))
        cand.append(X - math.ceil(i/2))
        break
  if len(cand) == 0:
    if N % 2 == 0:
      cand.append(X + int(N/2))
      cand.append(X - int(N/2))
    else:
      cand.append(X + int((N+1)/2))
      cand.append(X - int((N+1)/2))

  print(min(list(filter(lambda c: c not in P, cand))))