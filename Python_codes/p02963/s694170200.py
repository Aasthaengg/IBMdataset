import math
 
S = int(input())
 
 
X1 = 0
Y1 = 0
X2 = 10 ** 9
X3 = 1
 
Y3 = math.ceil(S / (10 ** 9))
Y2 = X2 * Y3 - S
 
print(X1, Y1, X2, Y2, X3, Y3)