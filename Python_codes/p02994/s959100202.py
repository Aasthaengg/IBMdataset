import numpy as np
N,L  = map(int,input().split())
L_list=np.array(range(1,N+1))+L-1
if (0 in L_list):
    print(sum(L_list))
    exit()
if(N<=abs(L) and L<0):
    print(sum(L_list)-L_list[N-1])
    
    exit()
else:
    print(sum(L_list)-L_list[0])
    exit()