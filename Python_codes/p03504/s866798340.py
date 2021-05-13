N,C=map(int,input().split())
L=[list(map(int,input().split())) for _ in range(N)]
L.sort()
stc=[[] for _ in range(C)]
for i in range(N):
  s,t,c=L[i]
  if stc[c-1] and s-stc[c-1][-1][1]<=1:
    stc[c-1][-1]=[stc[c-1][-1][0],t]
  else:
    stc[c-1].append([s-1,t])

STC=[j for i in stc for j in i]
STC.sort()

RCM=[[0,0] for _ in range(C)]
for S,T in STC:
  for i in range(C):
    if RCM[i][1]<=S:
      RCM[i][1]=T
      break

for i in range(C):
  if RCM[i]==[0,0]:
    print(i)
    exit()
print(C)