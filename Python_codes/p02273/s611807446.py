# ALDS1_5_C Koch Curve
import math

def koch(i, p, q):
    if i == n:
        print(' '.join(map(str, p)))
        if q[0] == 100:
            print(' '.join(map(str, q)))
        return

    x1 = (2 * p[0] + q[0]) / 3
    y1 = (2 * p[1] + q[1]) / 3
    x2 = (p[0] + 2 * q[0]) / 3
    y2 = (p[1] + 2 * q[1]) / 3

    x3 = math.cos(math.radians(60)) * (x2 - x1) - math.sin(math.radians(60)) * (y2 - y1) + x1
    y3 = math.sin(math.radians(60)) * (x2 - x1) + math.cos(math.radians(60)) * (y2 - y1) + y1

    koch(i + 1, p, [x1, y1])
    koch(i + 1, [x1, y1], [x3, y3])
    koch(i + 1, [x3, y3], [x2, y2])
    koch(i + 1, [x2, y2], q)


n = int(input())

koch(0, [0, 0], [100, 0])





