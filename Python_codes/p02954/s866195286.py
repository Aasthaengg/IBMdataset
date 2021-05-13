def f(S):
    if S=="R":
        return 1
    else:
        return -1

S=input()
N=len(S)
K=20
L=list(map(f,S))

A=[[0]*N for _ in range(K)]

for i in range(N):
    A[0][i]=i+L[i]

for k in range(1,K):
    for x in range(N):
        A[k][x]=A[k-1][A[k-1][x]]

Z=[0]*(N)
for k in range(N):
    P=10**6
    a=k
    i=0
    while P>0:
        if P%2:
            a=A[i][a]
        i+=1
        P>>=1
    Z[a]+=1

print(" ".join(map(str,Z)))
