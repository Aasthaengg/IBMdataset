from numba import jit
import numpy as np


n, k = map(int, input().split())
A = np.array([*map(int, input().split())],dtype=np.int64)

# for _ in range(min(k,int(math.log(n,2)))):

@jit
def loop(A):
    for _ in range(k):
        b=np.zeros(n,dtype=np.int64)
        
        for i,v in enumerate(A):
            # if i>v:
            b[max(0,i-v)]+=1
                # b[i-v]+=1
            # else:
                # b[0]+=1
            # j=i-~v
            if i+v+1<n:
                b[i+v+1]-=1
            # if j<n:
            #     b[j]-=1
        
        # update ans
        # cnt=0
        # for i in range(1,n):
        #     b[i]+=b[i-1]
        A=np.cumsum(b)
        
        if min(A)==n:
            break
    return A
print(" ".join(map(str,loop(A))))