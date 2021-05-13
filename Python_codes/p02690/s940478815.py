import math
X = int(input())

d =math.floor(math.pow(X, 1.0/4.0))
for i in range(-d-1,d+1,1):
    for j in range(-d-1,d+1,1):
        if X+j**5==i**5:
            print(i,j)
            exit()