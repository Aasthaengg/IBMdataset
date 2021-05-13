import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def d(p1, p2):
    a = p2.x - p1.x
    b = p2.y - p1.y
    c = math.sqrt(a * a + b * b)
    return(c)

data = [float(i) for i in input().split()]
p1 = Point(data[0], data[1])
p2 = Point(data[2], data[3])
print(d(p1,p2))
