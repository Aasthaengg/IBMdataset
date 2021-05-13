import sys
H, W, M = map(int, input().split())
hn = [0]*H
wn = [0]*W
flag = set()
for i in range(M):
  h, w = map(int, input().split())
  hn[h-1] += 1
  wn[w-1] += 1
  flag.add((h,w))
  
#hrank = sorted(hn, key=lambda t:-t[1])
#wrank = sorted(wn, key=lambda t:-t[1])

hmax = max(hn)
wmax = max(wn)

hmaxlist = {i+1 for i,h in enumerate(hn) if h == hmax}
#for h in hn:
#  if h == hmax:
#    hmaxlist.append(h)
  
wmaxlist = {i+1 for i,w in enumerate(wn) if w == wmax}
#for w in wn:
#  if w == wmax:
#    wmaxlist.append(w)
  

for i in hmaxlist:
  for j in wmaxlist:
    if (i,j) not in flag:
      print(hmax+wmax)
      sys.exit()
print(hmax+wmax-1)