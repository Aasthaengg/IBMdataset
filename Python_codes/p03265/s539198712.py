import numpy as np
X1,Y1,X2,Y2 = (int(T) for T in input().split())
MoveV  = np.array([X2-X1,Y2-Y1]).T
Rotate = np.array([[0,-1],[1,0]])

MoveV = np.dot(Rotate,MoveV)
X3,Y3 = X2+MoveV[0],Y2+MoveV[1]

MoveV = np.dot(Rotate,MoveV)
X4,Y4 = X3+MoveV[0],Y3+MoveV[1]

print('{} {} {} {}'.format(X3,Y3,X4,Y4))