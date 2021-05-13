import sys

N,C = map(int,input().split())
STC = []
for _ in range(N):
  s,t,c = map(int,sys.stdin.readline().split())
  STC.append([s,t,c])
STC.sort()

rs = [[STC[0][1],STC[0][2]]]
for i in range(1,N):
  len_rs = len(rs)
  
  min_idx = None
  for j in range(len_rs):
    if rs[j][1] != STC[i][2]: tmp_stc_r = STC[i][0] - 0.5
    else: tmp_stc_r = STC[i][0]
 
    if rs[j][0] <= tmp_stc_r:
      if min_idx is None: min_idx = j
      else:
        if rs[j][0] < rs[min_idx][0]: min_idx = j

  if min_idx is None: rs.append([STC[i][1], STC[i][2]])
  else: rs[min_idx] = [STC[i][1], STC[i][2]]
  
print(len(rs))