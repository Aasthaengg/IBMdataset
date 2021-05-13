import numpy as np
a,b,c,d = map(int,input().split())
X1 = np.array([a,b])
X2 = np.array([c,d])
x = (X2-X1)
x[0],x[1] = -x[1],x[0]
print((X2+x)[0],(X2+x)[1],(X1+x)[0],(X1+x)[1])