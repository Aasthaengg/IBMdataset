a = [int(s) for s in input().split()]
b = a[0] + a[1]
c = a[1] + a[2]
d = a[2] + a[0]
print(int(min([b,c,d])))