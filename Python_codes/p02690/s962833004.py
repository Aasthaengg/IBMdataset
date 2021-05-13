import math
import sys
X=int(input())
A=-200
B=-200

for i in range(400):
    for j in range(400):
        if A**5-B**5==X:
            print(A,B)
            sys.exit()
        A+=1
    A=-200
    B+=1