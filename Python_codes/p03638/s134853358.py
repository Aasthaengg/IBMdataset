from collections import deque

H,W=map(int,input().split())
n=int(input())
A=list(map(int,input().split()))
C=[]
for i in range(n):
    for _ in range(A[i]):
        C.append(i+1)


M=[deque([]) for _ in range(H)]

for i in range(H*W):
    if (i//W)%2==0:
        M[i//W].append(C[i])
    else:
        M[i//W].appendleft(C[i])

for i in range(H):
    print(*M[i])