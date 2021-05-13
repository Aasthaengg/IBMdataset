l = list(map(int,input().split()))
l.sort()
a = l[0]
b = l[1]
c = l[2]
if a%2 == 0 or b%2 == 0 or c%2 == 0:
    print(0)
    exit(0)
vmax,vmin = 0,0
v = a*b*c
vmin = (c//2)*a*b
vmax = v - vmin
print(vmax-vmin)

