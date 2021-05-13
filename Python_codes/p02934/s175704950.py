import numpy as np
n=int(input())
a=np.array(list(map(int,input().split())))
a=1/a
print(1/sum(a))