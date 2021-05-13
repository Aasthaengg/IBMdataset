from itertools import accumulate
from operator import add

N,K = map(int,input().split())
A = map(int,input().split()) 
for k in range(K):
    B = [0] * N
    for i,x in enumerate(A):
        L = max(0, i-x)
        R = min(N-1, i+x)
        B[L] += 1
        if R+1 != N:
            B[R+1] -= 1
    L = list(accumulate(B,add)) 
    #L = list(accumulate(B))[:]
    if L == A:
        break
    A = L
print(*A)    