ns=input()

nsl=ns.split(' ')

nsc=[]
for i in range(3):
  nsc.append(nsl.count(nsl[i]))

if nsc[0]==nsc[1]==nsc[2]==1:
  print('3')
elif nsc[0]==2 or nsc[1]==2:
  print('2')
else:
  print('1')