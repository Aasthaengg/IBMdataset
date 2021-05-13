from itertools import combinations

h,w,k=map(int,input().split())
G=[]
for _ in range(h):
  s=input()
  S=[]
  for i in range(w):
    S.append(s[i])
  G.append(S)
ans=0

HH=[]
for i in range(1<<h):
  H=[]
  for j in range(h):
    if (i>>j)&1:
      H.append(j)
  HH.append(H)

WW=[]
for i in range(1<<w):
  W=[]
  for j in range(w):
    if (i>>j)&1:
      W.append(j)
  WW.append(W)

for i in range(1<<h):
  for j in range(1<<w):
    cnt=0
    hl=HH[i]
    wl=WW[j]
    for m in range(h):
      for n in range(w):
        if m in hl:
          continue
        if n in wl:
          continue
        if G[m][n]=='#':
          cnt+=1
    if cnt==k:
      ans+=1
print(ans)