x = input()
x = input()
x = x.split(" ")
x = [int(z) for z in x]
cmax = -1000000
cmin = 1000000
csum = 0
for z in x:
    if cmax < z:
        cmax = z
    if cmin > z:
        cmin = z
    csum += z
print("%d %d %d" % (cmin, cmax, csum))