from collections import Counter
H,W,*L = open(0).read().split()
H,W = map(int, (H,W))
s = ''
for c in L:
  s += c
Cnt = Counter(s)
g1 = 0
g2 = 0
g3 = 0
if H%2==1 and W%2==1:
  g1 = 1
  g2 = H//2+W//2
  g3 = (H//2)*(W//2)
elif H%2==1:
  g1 = 0
  g2 = W//2
  g3 = (H//2)*(W//2)
elif W%2==1:
  g1 = 0
  g2 = H//2
  g3 = (H//2)*(W//2)
else:
  g1 = 0
  g2 = 0
  g3 = (H//2)*(W//2)

while g3:
  for k in Cnt.keys():
    if Cnt[k]>=4:
      Cnt[k] -= 4
      g3 -= 1
      break
  else:
    break
  
while g2:
  for k in Cnt.keys():
    if Cnt[k]>=2:
      Cnt[k] -= 2
      g2 -= 1
      break
  else:
    break
  
while g1:
  for k in Cnt.keys():
    if Cnt[k]>=1:
      Cnt[k] -= 1
      g1 -= 1
      break
  else:
    break

if all(Cnt[k]==0 for k in Cnt.keys()):
  print('Yes')
else:
  print('No')