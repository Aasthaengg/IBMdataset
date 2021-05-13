n = int(input())
p = -10 ** 10
rmin= 10 ** 10
while n > 0:
    r = int(input())
    if n == 0:
        rmax = r
    else:
        if r - rmin > p:
            p = r - rmin
        if r < rmin:
            rmin = r
    n -= 1
print(p)