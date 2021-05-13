import numpy as np
W,H,N=map(int,input().split())
A=np.zeros((W,H))
B=[list(map(int,input().split())) for _ in range(N)]
for b in B:
    if b[2]==1:
        A[:b[0],:]=1
    elif b[2]==2:
        A[b[0]:,:]=1
    elif b[2]==3:
        A[:,:b[1]]=1
    elif b[2]==4:
        A[:,b[1]:]=1
print(np.count_nonzero(A==0))