import numpy as np
N = int(input())
A = list(map(int,input().split()))
B = [0]*N
ans =0 
for i,j in enumerate(A):
    B[i] = j-(i+1)
B=sorted(B)
b=np.median(np.array(B))
for i,j in enumerate(A):
    ans+= abs(j-(int(b)+i+1))
print(ans)