from numpy import *
from scipy.sparse.csgraph import *
H,W,*t=map(int,open(0).read().split())
c=array(t[:100]).reshape((10,10))
A=array(t[100:])
print(int(sum(shortest_path(c)[:,1][A[A>=0]])))