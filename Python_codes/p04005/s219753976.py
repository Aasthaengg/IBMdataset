BOX = [int(j) for j in input().split(' ')]
if len([j for j in BOX if j % 2 == 0]) > 0:
    print(0)
else:
    BOX = [BOX[0] * BOX[1],BOX[1]*BOX[2],BOX[0]*BOX[2]]
    BOX.sort()
    print(BOX[0])
