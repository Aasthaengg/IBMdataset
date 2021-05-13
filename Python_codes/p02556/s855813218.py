n = int (input())

xy = []

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
for i in range(n):
    x, y = map(int,input().split())
    xy.append([x+y, x-y])

xy.sort(key = lambda x: x[0])

min_z = xy[0][0]
max_z = xy[-1][0]

xy.sort(key = lambda x: x[1])

min_w = xy[0][1]
max_w = xy[-1][1]

print(max(abs(min_z - max_z), abs(min_w - max_w)))
