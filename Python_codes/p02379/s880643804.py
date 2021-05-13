import math

def distance(a, b):
    dx = abs(a[0]-b[0])
    dy = abs(a[1]-b[1])
    return math.sqrt(dx*dx + dy*dy)

if __name__ == '__main__':
    x1, y1, x2, y2 = map(float, input().split())
    print(distance((x1, y1), (x2, y2)))

