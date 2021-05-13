import numpy as np
X = np.array([list(map(int, input().split())) for _ in range(3)])
T = True
if X[0][0]-X[0][1]==X[1][0]-X[1][1]==X[2][0]-X[2][1]\
   and X[0][1]-X[0][2]==X[1][1]-X[1][2]==X[2][1]-X[2][2]:
    pass
else:
  T = False

X = X.T
if X[0][0]-X[0][1]==X[1][0]-X[1][1]==X[2][0]-X[2][1]\
   and X[0][1]-X[0][2]==X[1][1]-X[1][2]==X[2][1]-X[2][2]:
    pass
else:
  T = False
print("Yes" if T else "No")