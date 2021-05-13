N,A,B=map(int,input().split())
X=list(map(int,input().split()))
import numpy as np
X=np.array(X)
print(sum(np.minimum((X[1:]-X[:N-1])*A , B)))