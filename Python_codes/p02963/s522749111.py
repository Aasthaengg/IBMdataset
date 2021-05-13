import math

S = int(input())

sqrtS = math.ceil(math.sqrt(S))
rest = sqrtS*sqrtS - S

X1,Y1 = 0,0
X2,Y2 = sqrtS, 1
X3,Y3 = rest, sqrtS
print("{} {} {} {} {} {}".format(X1,Y1,X2,Y2,X3,Y3))

