x = input()
x = '000'+x
z = x[:-2]
y = x[-2:]
s = 0
z = int(z)
y = int(y)
L = []
y1 =y//5
if z>=20 or z>=(y1+(y%5!=0)):
    print(1)
    exit()
print(0)