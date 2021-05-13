W,H,N=list(map(int, input().split()))
wl=[0]
wh=[W]
hl=[0]
hh=[H]
for i in range(N):
  l=list(map(int, input().split()))
  if l[2]==1:
    wl.append(l[0])
  elif l[2]==2:
    wh.append(l[0])
  elif l[2]==3:
    hl.append(l[1])
  else:
    hh.append(l[1])
w=min(wh)-max(wl)
h=min(hh)-max(hl)
if w>0 and h>0:
  print(w*h)
else:
  print(0)