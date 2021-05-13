import numpy as np
s=int(input())

x2=int(np.ceil(np.sqrt(s)))
y3=x2

res=x2*y3-s

print('0 0 {} 1 {} {}'.format(x2,res,y3))