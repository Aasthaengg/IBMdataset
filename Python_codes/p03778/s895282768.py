import sys
import math
W,a,b = map(int,input().split())
al = [[a,0],[a,1],[a+W,0],[a+W,1]]
bl = [[b,1],[b,2],[b+W,1],[b+W,2]]
box = []
if (b <= a and a <= b+W) or (a <= b <= a+W and a <= b+W <=a+W) or (a <= b and b <= a+W):
  print(0)
  sys.exit()
for i in range(4):
  for j in range(4):
    num = math.sqrt((al[i][0]-bl[j][0])**2 + (al[i][1]-bl[j][1])**2)
    box.append(int(num))
print(min(box))