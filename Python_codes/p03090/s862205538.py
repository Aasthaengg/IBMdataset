import sys
N=int(input())
if N%2==1:
    L=[]
    for i in range(1,N):
        for j in range(i,N):
            if i==j or i+j==N:
                continue
            L.append((i,j))
    for i in range(1,N):
        L.append((i,N))
    print(len(L))
    for a,b in L:
        print(a,b)
else:
    L=[]
    for i in range(1,N+1):
        for j in range(i,N+1):
            if i==j or i+j==N+1:
                continue
            L.append((i,j))
    print(len(L))
    for a,b in L:
        print(a,b)