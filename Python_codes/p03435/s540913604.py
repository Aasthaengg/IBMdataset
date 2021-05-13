import sys
c=[list(map(int,l.split())) for l in sys.stdin.read().splitlines()]
for i in range(2):
  c[2-i]=[x-y for x, y in zip(c[2-i],c[1-i])]
for i in range(2):
  for j in range(3):
    c[j][2-i]-=c[j][1-i]

if c[1][1:]==c[2][1:]==[0,0]:
  print('Yes')
else:
  print('No')