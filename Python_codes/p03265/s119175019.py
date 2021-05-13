import math
x1, y1, x2, y2 = list(map(lambda a: int(a), input().split(" ")))
P1 = [x1, y1]
P2 = [x2, y2]
L12 = [P2[0] - P1[0], P2[1] - P1[1]]
L23 = [-L12[1], L12[0]]
P3 = [P2[0] + L23[0], P2[1] + L23[1]]
P4 = [P3[0] - L12[0], P3[1] - L12[1]]

print(" ".join([str(P3[0]), str(P3[1]), str(P4[0]), str(P4[1])]))