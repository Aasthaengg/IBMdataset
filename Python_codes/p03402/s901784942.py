import numpy as np
A,B = map(int,input().split())

mat = np.zeros((100,100),dtype=bool)

if A<=B:
    black = "."
    white = "#"
else:
    black = "#"
    white = "."

A,B = min(A,B),max(A,B)

a = A-1
b = B-1

for i in range(100):
    mat[0][i] = 1
for i in range(100):
    mat[1][i] = i%2

for line in range(2,100):
    if a>=50 and b>=50:
        for j in range(100):
            mat[line][j] = not(line%2 ^ j%2)
        a-=50
        b-=50
    elif a>0:
        for j in range(a*2):
            mat[line][j] = not(line%2 ^ j%2)
        b-=a
        a = 0
    else:
        break
for line in range(99,2,-2):
    if b>=50:
        for j in range(100):
            mat[line][j] = (j%2)
        b -= 50
    elif b>0:
        for j in range(b*2):
            mat[line][j] = (j%2)
        b = 0
    else:
        break

print("100 100")
for i in range(100):
    for j in range(100):
        if not mat[i][j]:
            print(black,end="")
        else:
            print(white,end="")
    print("")

