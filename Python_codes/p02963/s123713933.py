s = int(input())
thld = pow(10,9)
x = (thld-s%thld)%thld
print(0, 0, thld, 1, x, (s+x)//thld)