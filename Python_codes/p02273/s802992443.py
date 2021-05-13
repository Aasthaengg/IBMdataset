import math

def koch(p1, p2, dp):

    if dp == 0:
        return
    
    sX = (p2[0] - p1[0]) / 3 + p1[0]
    sY = (p2[1] - p1[1]) / 3 + p1[1]
    s = (sX, sY)

    tX = (p2[0] - p1[0]) * 2 / 3 + p1[0]
    tY = (p2[1] - p1[1]) * 2 / 3 + p1[1]
    t = (tX, tY)

    uX = (tX - sX) * math.cos(math.radians(60)) - (tY - sY) * math.sin(math.radians(60)) + sX
    uY = (tX - sX) * math.sin(math.radians(60)) + (tY - sY) * math.cos(math.radians(60)) + sY
    u = (uX, uY)

    koch(p1, s, dp - 1)
    myPrint(s)
    koch(s, u, dp - 1)
    myPrint(u)
    koch(u, t, dp - 1)
    myPrint(t)
    koch(t, p2, dp - 1)

    
def myPrint(val):
    print("{:.8f} {:.8f}".format(val[0], val[1]))
    

n = int(input())

p1 = (0.0, 0.0)
p2 = (100.0, 0.0)

myPrint(p1)
koch(p1, p2, n)
myPrint(p2)
