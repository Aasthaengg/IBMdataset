MM = input().split()
N = int(MM[0])
M = int(MM[1])
X = int(MM[2])
Y = int(MM[3])
xx = input().split()
yy = input().split()
xxx =[]
yyy =[]
for i in xx:
  xxx.append(int(i))
for i in yy:
  yyy.append(int(i))
xxx.sort()
yyy.sort()
count =0
for i in range(X+1,Y+1):
  if xxx[-1] < i and yyy[0] >= i:
    count +=1
    
if count == 0:
  print('War')
else:
  print('No War')