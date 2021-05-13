a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = a+b
f = c+d
if e > f:
    print ("Left")
if e == f:
    print("Balanced")
if e < f:
    print ("Right")
