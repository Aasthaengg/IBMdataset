a=input().split(" ")
x1=""
x2=""

for j in range(int(a[0])):
    x1=x1+a[1]

for y in range(int(a[1])):
    x2=x2+a[0]

z1=int(x1)
z2=int(x2)

if x1<x2:
	print(x1)
elif x1>x2:
	print(x2)
else:
	print(x1)




