import numpy as np
N,M = map(int, input().split())
S = []
for i in range(M):
    k,*s = map(int, input().split())
    T = [0]*N
    for j in s:
        T[j-1]=1
    S.append(T)
P = list(map(int, input().split()))
ans =0
for x in range(2**N):
    y = format(x,"0{}b".format(N))
    z = list(map(int,y))
    if all(np.dot(den,z)%2==P[nmb] for nmb,den in enumerate(S)):
        ans +=1
            
print(ans)   