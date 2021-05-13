import numpy as np
N,Q = map(int,input().split())
S = input()
T = (N+1)*[0]

for n in range(N):
  if S[n:n+2]=="AC":
    T[n+1]+=1

T = np.cumsum(T)

for q in range(Q):
  l,r = map(int,input().split())
  print(T[r-1]-T[l-1])