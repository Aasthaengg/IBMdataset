N = [int(e) for e in input().split()]
a = N[0]
b = N[1]
c = N[2]
d = N[3]
if(a*b) > (c*d):
    print(a*b)
else:
    print(c*d)