import math

n = int(input())

dots = [[0,0],[100,0]]
for _ in range(n):
    producedDots = []
    for i in range(len(dots)-1):
        pointA = [dots[i][0] + (dots[i+1][0]-dots[i][0])/3, dots[i][1] + (dots[i+1][1]-dots[i][1])/3]
        pointB = [dots[i][0] + (dots[i+1][0]-dots[i][0])*2/3, dots[i][1] + (dots[i+1][1]-dots[i][1])*2/3]

        producedDots.append(dots[i])
        producedDots.append(pointA)

        arrow = [pointB[0]-pointA[0], pointB[1]-pointA[1]]
        cos60 = math.cos(math.radians(60))
        sin60 = math.sin(math.radians(60))
        newArrow = [arrow[0]*cos60 - arrow[1]*sin60, arrow[0]*sin60 + arrow[1]*cos60]
        pointC = [pointA[0] + newArrow[0], pointA[1] + newArrow[1]]
        producedDots.append(pointC)

        producedDots.append(pointB)
    dots = producedDots
    dots.append([100,0])

for _ in dots:
    print(" ".join(map(str,_)))
