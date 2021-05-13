import sys


def calc(i1, i2):

    a = i1
    b = i2
    if (i1 < i2):
        a = i2
        b = i1
    
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    gcd = b
    lcm = (i1 * i2) / gcd

    return gcd, lcm


for line in sys.stdin:
    datas =line.split()
    if (len(datas)):

        li = list(map(int, datas)) 
        a = li[0]
        b = li[1]

        x, y = calc(a, b)

        print("%d %d" % (x, y))

    else:
        break