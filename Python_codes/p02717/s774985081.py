x,y,z = map(int, input().split())
x,y = y,x
x,z = z,x
print("{} {} {}".format(x,y,z))