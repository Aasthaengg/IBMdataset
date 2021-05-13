a,b = map(int,input().split())

x = a // b
y = a % b
z = a / b

print(x,end=" ")
print(y,end=" ")
print("{0:.20f}".format(z))