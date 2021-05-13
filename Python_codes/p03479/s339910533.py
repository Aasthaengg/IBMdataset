import numpy as np

x,y=list(map(int,input().split()))

print(np.floor(np.log2(y//x,dtype=np.longdouble)).astype(np.int)+1)