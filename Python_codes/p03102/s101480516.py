import numpy as np
N,M,C=map(int,input().split())
B=np.array([int(i) for i in input().split()])
A=np.array([[int(i) for i in input().split()] for j in range(N)])

ans=np.count_nonzero(np.dot(A,B)>-C)
print(ans)