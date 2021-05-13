n = int(input())
a = list(map(int, input().split()))

flag = [False]*8
t = 0
for i in a:
  if i < 400: flag[0] = True
  elif i < 800: flag[1] = True
  elif i < 1200: flag[2] = True
  elif i < 1600: flag[3] = True
  elif i < 2000: flag[4] = True
  elif i < 2400: flag[5] = True
  elif i < 2800: flag[6] = True
  elif i < 3200: flag[7] = True
  elif 3200 <= i: t += 1
    
minNum = 0
p = flag.count(True)
if p > 0: minNum = p
elif p == 0 and t > 0:
  minNum = 1
  
maxNum = p + t

print(minNum,maxNum)