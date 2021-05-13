import numpy as np
N, C = map(int, input().split())
dic = []
L = 0
for i in range(N):
  s, t, c = map(int, input().split())
  dic += [(c-1,s,t)]
  if 2*t+1>L:
    L = 2*t+1

sm = np.zeros(L)
for c in range(C):
  tt = np.zeros(L)
  for i in range(N):
    if dic[i][0]==c:
      tt[dic[i][1]*2-1] += 1
      tt[dic[i][2]*2] -= 1
  tt = tt.cumsum()
  sm[tt>0] += 1
print(int(sm.max()))