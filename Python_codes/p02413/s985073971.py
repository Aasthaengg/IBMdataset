from operator import add
from functools import reduce

r,c = map(int,input().split())

x = [list(map(int, input().split())) for i in range(r)]


#import numpy as np


#x=[[3,4,5],[1,2,3]]
#a=np.array(x)
#print(a)
#b=reduce(add, a)
#print(b)
#b=list(b)

#x=list(x[1])
#x.append(b)

#print(x)


b = []

for j in range(c):
    a = [x[i][j] for i in range(len(x))]
    b.append(reduce(add,a))

#print(b)

x.append(b)

for i in range(len(x)):
    y = reduce(add,x[i])
    x[i].append(y)
    
    
z = [list(map(str,x[i])) for i in range(len(x))]

#print(z)
#print(z)

w = [' '.join(z[i]) for i in range(len(x))]

[print(w[i]) for i in range(len(w))]

