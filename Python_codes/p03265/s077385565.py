x1, y1, x2, y2 = map(int, input().split())

def dot0(x, y, v):
    return (x - v[1], y + v[0])
    
vector = (x2 - x1, y2 - y1)
x3, y3 = dot0(x2, y2, vector)
x4, y4 = dot0(x1, y1, vector)

print(x3, y3, x4, y4)