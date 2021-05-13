n = int(input())
a = list(map(int, input().split()))

a.sort()

colors = [0,0,0,0,0,0,0,0]
mulch = 0

for i in a:
  if i < 400:
    colors[0] += 1
  elif i < 800:
    colors[1] += 1
  elif i < 1200:
    colors[2] += 1
  elif i < 1600:
    colors[3] += 1
  elif i < 2000:
    colors[4] += 1
  elif i < 2400:
    colors[5] += 1
  elif i < 2800:
    colors[6] += 1
  elif i < 3200:
    colors[7] += 1
  else:
    mulch += 1
    
if len([j for j in colors if j > 0]) > 0:
  mi = len([j for j in colors if j > 0])
else:
  mi = 1

if mulch > 0:
  if len([j for j in colors if j > 0]) == 0:
    ma = mulch
  else:  
    ma = mi + mulch
else:
  ma = mi
  
print(mi, ma)