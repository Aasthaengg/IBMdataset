a=input()

b=a.split(' ')

c=[]

for i in range(3):
  c.append(int(b[i]))

if c[1]-c[0]==c[2]-c[1]:
  print('YES')
else:
  print('NO')