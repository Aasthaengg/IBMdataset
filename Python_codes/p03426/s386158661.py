H,W,D = map(int,input().split())

A = [[0]*W for i in range(H)]
data = [0]*(H*W+1)

for i in range(H):
    A[i] = list(map(int,input().split()))

for i in range(H):
    for j in range(W):
        data[A[i][j]] = [i,j]

Q = int(input())

L = [0] * Q
R = [0] * Q

for i in range(Q):
    L[i],R[i] = map(int,input().split())

X = [0]*(H*W+1)

for i in range(D):
    x = H*W-D-i
    count = 0
    while x > 0:
        count += abs(data[x][0]-data[x+D][0])+abs(data[x][1]-data[x+D][1])
        X[x] += count
        x -= D

for i in range(Q):
    print(X[L[i]]-X[R[i]])