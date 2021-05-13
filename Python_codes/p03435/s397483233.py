import sys
c=[list(map(int,input().split())) for _ in range(3)]

for i in range(min(c[0])+1):
  b=[c[0][k]-i for k in range(3)]
  a=[c[i][0]-b[0] for i in range(3)]
  for i in range(1,3):
    if c[i][1]!=a[i]+b[1] or c[i][2]!=a[i]+b[2]:
        break
  else:
    print('Yes')
    sys.exit()
print('No')