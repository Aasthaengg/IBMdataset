a, b = [float(i) for i in input().split()]
print("{0} {1} {2:10f}".format(int(a//b), int(a%b), a/b))