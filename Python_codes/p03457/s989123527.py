import math
n = int(input())
#P position t time
P = [0,0]
t0 = 0
for _ in range(n):
  t,x,y = map(int, input().split( ))
  dt = t - t0
  dis = abs(x - P[0])  + abs(y - P[1])
  if dis > dt:
    print('No')
    exit()
  elif (dt - dis)%2 == 1:
    print('No')
    exit()
  t0 = t
  P = [x,y]
print('Yes')
    
