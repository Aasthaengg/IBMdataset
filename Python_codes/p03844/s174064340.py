ns=input()
nsl=ns.split(' ')

if nsl[1]=='+':
  print(int(nsl[0])+int(nsl[2]))
else:
  print(int(nsl[0])-int(nsl[2]))