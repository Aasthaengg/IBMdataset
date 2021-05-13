import numpy as np

n,k=map(int,input().split())
h=np.array(list(map(int,input().split())))

print(np.count_nonzero(h-k>=0))
