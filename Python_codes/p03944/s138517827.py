import numpy as np

W, H, N = input().split()
commands = []
for i in range(int(N)):
  commands.append(input().split())
pic = np.zeros((int(W),int(H)))
for com in commands:
  x = int(com[0])
  y = int(com[1])
  a = int(com[2])
  if a==1:
    pic[:x,:] = 1
  if a==2:
    pic[x:,:] = 1
  if a==3:
    pic[:,:y] = 1
  if a==4:
    pic[:,y:] = 1

area = 0

for w in range(int(W)):
  for h in range(int(H)):
    if pic[w,h]==0:
      area += 1
      
print(area)