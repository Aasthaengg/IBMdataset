a=input()
b=a.split(' ')
c=[]

for i in range(2):
  c.append(int(b[i]))

print((c[0]+c[1])%24)