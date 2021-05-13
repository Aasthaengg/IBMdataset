[x1,y1,x2,y2] = [int(i) for i in input().split()]

vector = [x2 - x1, y2 - y1]
vector_t = [y1 - y2,x2 - x1]
x3 = x2 + vector_t[0]
y3 = y2 + vector_t[1]
x4 = x3 - vector[0]
y4 = y3 - vector[1]

print(x3,y3,x4,y4)
