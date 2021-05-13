def rect(a,b):
    return a*b, 2*(a+b)
n =input()
x =n.split()
a =int(x[0])
b =int(x[1])

area, perimeter =rect(a,b)
print(area, perimeter)
