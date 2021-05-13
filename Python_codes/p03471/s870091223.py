x = list(map(int, input().split()))
ans = 0
man = 0
gosen = 0
sen = 0
y = x[0]+1
for i in range(y):
  for j in range(y-i):
    if i*10000+j*5000+(x[0]-i-j)*1000 == x[1]:
      man = i
      gosen = j
      sen = x[0]-i-j
      ans = 1
      break
if ans == 1:
  print(str(man)+' '+str(gosen)+' '+str(sen))
else:
  print('-1 -1 -1')