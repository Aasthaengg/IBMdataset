a,b=input().split()
x=''
y=''
for i in range(int(b)):
  x+=a
for i in range(int(a)):
  y+=b

l=[x,y]

l.sort()

print(l[0])


