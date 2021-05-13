from collections import defaultdict
X,Y = list(map(int,input().split()))
M = defaultdict(int)
M[3] = 100000
M[2] = 200000
M[1] = 300000
sm = 0
sm += M[X]
sm += M[Y]
if X == Y == 1:
    sm += 400000
print(sm)