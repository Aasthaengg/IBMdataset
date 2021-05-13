from collections import deque

n = int(input())
points = [0 for i in range(n)]

class Point:
    def __init__(self, number, arrow):
        self.number = number        
        self.arrow = arrow
        self.destination = []
        self.distance = -1
        self.hadSearched = False

for i in range(n):
    L = list(map(int, input().split()))
    points[i] = Point(i+1, L[1])
    if L[1] >= 1:
        points[i].destination = L[2:]

def bfs(coord):
    dq = deque()
    coord.hadSearched = True
    dq.appendleft((0, coord))

    while dq:
        steps, po = dq.pop()
        po.distance = steps

        if len(po.destination) > 0:
            for des in po.destination:
                if points[int(des)-1].hadSearched == False:
                    points[int(des)-1].hadSearched = True
                    dq.appendleft((steps+1, points[int(des)-1]))

bfs(points[0])

for i in range(n):
    print("{} {}".format(i+1, points[i].distance))
