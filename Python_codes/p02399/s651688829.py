x = input().split()
a = int(x[0])
b = int(x[1])
d = a // b
r = a % b
f = '{:.6f}'.format(a/b)
print(d,r,f)
