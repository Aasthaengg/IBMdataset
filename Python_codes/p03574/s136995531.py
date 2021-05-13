h,w=map(int,input().split())
gf=[['.']+list(input())+['.'] for _ in range(h)]
gf=[['.']*(w+2)]+gf+[['.']*(w+2)]
for i in range(1,h+1):
  for j in range(1,w+1):
    if gf[i][j]!='#':
      gf[i][j]=str([gf[i+s][j+t] for s in range(-1,2) \
                    for t in range(-1,2) if i!=0 or j!=0].count('#'))
for i in range(1,h+1):
  print(''.join(gf[i][1:w+1]))