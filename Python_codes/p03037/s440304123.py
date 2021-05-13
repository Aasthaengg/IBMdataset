N,M = map(int,input().split())
L_max,R_min = 0,10000000
for i in range(M):
  L,R = map(int,input().split())
  L_max = max(L_max,L)
  R_min = min(R_min,R)
if R_min < L_max:
  print(0)
else:
  print(R_min - L_max + 1)