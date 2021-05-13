NN = input().split()
N = int(NN[0])
M = int(NN[1])
AA = input().split()
total1 = 0
total2 = 0
for i in AA:
  total1 += int(i)
for i in AA:
  if float(i) >= total1/(4*M):
    total2 +=1
if total2 >= M:
  print('Yes')
else:
  print('No')