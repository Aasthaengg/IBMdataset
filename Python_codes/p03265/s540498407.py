x1, y1, x2, y2 = [int(i) for i in input().split()]

def rotate(x1, y1, x2, y2):
    return x2 - (y2 - y1), y2 + (x2 - x1)

x3, y3 = rotate(x1, y1, x2, y2)
x4, y4 = rotate(x2, y2, x3, y3)
print(x3, y3, x4, y4)