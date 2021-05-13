import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def recursive(pos):
    if len(pos) == 1:
        return 0
    dist = 0
    for p in range(len(pos) - 1):
        dist += distance(pos[0], pos[p + 1])
    dist += recursive(pos[1:])
    return dist

N = int(input())
pos = []
for i in range(int(N)):
    p = input().split(" ")
    pos.append([int(p[0]), int(p[1])])

print(recursive(pos) * 2 / N)
