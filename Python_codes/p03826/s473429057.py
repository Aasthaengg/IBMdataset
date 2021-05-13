ns=input()

nsl=ns.split(' ')

nl=[]

for i in range(4):
  nl.append(int(nsl[i]))

if nl[0]*nl[1]>=nl[2]*nl[3]:
  print(nl[0]*nl[1])
else:
  print(nl[2]*nl[3])