from math import pi, sin, cos

count = int(input())
p1 = [0,0]
p2 = [100,0]

def koch(p1, p2, count):

    if count == 0:
        return

    p3 = [ (2*p1[0] + p2[0]) / 3, (2*p1[1] + p2[1]) / 3]

    p5 = [ (p1[0] + 2*p2[0]) / 3, (p1[1] + 2*p2[1]) / 3]

    p4 = [ (p5[0]-p3[0])*cos(pi/3) - (p5[1]-p3[1])*sin(pi/3) + p3[0], \
        (p5[0]-p3[0])*sin(pi/3) + (p5[1]-p3[1])*cos(pi/3) + p3[1]] # なぜ

    koch(p1, p3, count - 1)
    print(*p3) # 配列の[]を外す
    koch(p3, p4, count - 1)
    print(*p4) # 配列の[]を外す
    koch(p4, p5, count - 1)
    print(*p5) # 配列の[]を外す
    koch(p5, p2, count - 1)

print(*p1)
koch(p1, p2, count)
print(*p2)
