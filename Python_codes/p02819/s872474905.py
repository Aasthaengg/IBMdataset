import sys
import copy
X = int(input())
while True:
    b = False
    for i in range(2,X):
        if X%i == 0:
            b = True
            break

    if b == False:
        print(X)
        sys.exit(0)
    else:
        X+=1
