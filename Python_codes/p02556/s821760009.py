import numpy as np

N = int(input())
XY = []
for i in range(N):
  XY.append([int(i) for i in input().split()])

XY = np.array(XY)
X = XY[:,0]
Y = XY[:,1]
pxpy = X + Y
pxmy = X - Y
mxpy =-X + Y
mxmy =-X - Y

candi = [np.argmax(pxpy),np.argmax(pxmy),np.argmax(mxpy),np.argmax(mxmy)]

cand = [XY[candi[i]] for i in range(4)]
manh = [abs(cand[0][0] - cand[3][0]) + abs(cand[0][1] - cand[3][1]), abs(cand[1][0] - cand[2][0]) + abs(cand[1][1] - cand[2][1])]
print(max(manh))