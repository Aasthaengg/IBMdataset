import numpy as np
c1 = list(map(int,input().split()))
A = np.array(c1)
c1 = list(map(int,input().split()))
B = np.array(c1)
c1 = list(map(int,input().split()))
C = np.array(c1)

D = A-B 
D1 = list(D)
D1 = set(D1)
if len(D1) == 1:
    pass 
else:
    print('No')
    exit()

E = B-C
E1 = list(E)
E1 = set(E1) 
if len(E1)== 1:
    print('Yes') 
else:
    print('No')