(a, b) = [int(x) for x in input().split()]

x = a // b
y = a % b
z = a / b

print(x,y,"{0:f}".format(z))