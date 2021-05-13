import numpy as np
from scipy.sparse.csgraph import connected_components
from collections import deque
n,m=map(int,input().split())
matrix=[[0]*n]*n
matrix=np.array(matrix)
l=deque()
for _ in range(m):
    a,b=map(int,input().split())
    l.append([a,b])
    matrix[a-1][b-1]=1
count=0
for i in range(m):
    [a,b]=l.popleft()
    matrix[a-1][b-1]=0
    k,kk=connected_components(matrix)
    if kk[a-1]!=kk[b-1]:
        count+=1
    l.append([a,b])
    matrix[a-1][b-1]=1
print(count)
