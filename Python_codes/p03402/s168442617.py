import numpy as np
A,B = map(int,input().split())
w = "."
b = "#"
if A<B:
    w,b = b,w
    A,B = B,A
Q1 = np.array([[b,b,b,b],[b,b,b,b],[b,b,b,b],[b,b,b,b]],dtype=np.unicode)
Q2 = np.array([[w,w,w,b],[w,w,w,b],[w,w,w,b],[b,b,b,b]],dtype=np.unicode)
Q3 = np.array([[w,w,w,b],[w,b,w,b],[w,w,w,b],[b,b,b,b]],dtype=np.unicode)
Grid = [[Q1]*25 for _ in range(20)]
B -= 1
for i in range(20):
    for j in range(25):
        if A:
            Grid[i][j] = Q2
            A -= 1
            if B:
                Grid[i][j] = Q3
                B -= 1
for i in range(20):
    if i == 0:
        AC = Grid[0][0]
    else:
        AC_ = Grid[i][0]
    for j in range(1,25):
        if i == 0:
            AC = np.hstack([AC,Grid[0][j]])
            continue
        AC_ = np.hstack([AC_,Grid[i][j]])
    if i != 0:
        AC = np.vstack([AC,AC_])
print(80,100)
for i in range(80):
    print(*AC[i],sep="")
