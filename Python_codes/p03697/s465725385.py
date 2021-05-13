
Tmp = []
Tmp = input().rstrip().split(' ')

nA = int(Tmp[0])
nB = int(Tmp[1])

nAns = nA + nB

if nAns > 9:
  print('error')
else:
  print(nAns)
