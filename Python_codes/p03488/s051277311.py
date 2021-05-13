s=input()
x,y=map(int,input().split())
#s='FT'*4
#x,y=2,2
if 'T' not in s:
  if len(s)==x and y==0:
    print('Yes')
  else:
    print('No')
else:
  move=s.split('T')
  xmove=[len(move[2*i+2]) for i in range((len(move)-1)//2)]
  ymove=[len(move[2*i+1]) for i in range(len(move)//2)]
  import numpy as np
  # 8000を0とする
  ablex=np.full(16001,False)
  abley=np.full(16001,False)
  ablex[8000+len(move[0])]=True
  abley[8000]=True
  for xi in xmove:
    if xi==0:continue
    ax=np.full(16001,False)
    ax[xi:]+=ablex[:-xi]
    ax[:-xi]+=ablex[xi:]
    ablex=ax
  for yi in ymove:
    if yi==0:continue
    ay=np.full(16001,False)
    ay[yi:]+=abley[:-yi]
    ay[:-yi]+=abley[yi:]
    abley=ay
  if ablex[8000+x] and abley[8000+y]:
    print('Yes')
  else:
    print('No')
  #print(ablex[8000:8005])
  #print(abley[8000:8005])