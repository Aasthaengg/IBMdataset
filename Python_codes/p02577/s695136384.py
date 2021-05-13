K=str(input())
SUM=0

for i in range(len(K)):
  SUM+=int(K[i])

if SUM%9==0:
  print('Yes')
else:
  print('No')
