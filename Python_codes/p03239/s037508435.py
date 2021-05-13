MM = input().split()
N = int(MM[0])
T = int(MM[1])
list1 =[]
for i in range(N):
  NN = input().split()
  c = int(NN[0])
  t = int(NN[1])
  if t <= T:
    list1.append(c)
list1.sort()
if len(list1) == 0:
  print('TLE')
else:
  print(list1[0])