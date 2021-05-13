H,W=map(int,input().split())

S=[[0]*(W+2) for _ in range(H+2)]
for i in range(H):
    S[i+1]=[0]+list(map(lambda x:int(x=="."),input()))+[0]


R=[[0]*(W+2) for _ in range(H+2)]
L=[[0]*(W+2) for _ in range(H+2)]
U=[[0]*(W+2) for _ in range(H+2)]
D=[[0]*(W+2) for _ in range(H+2)]


for y in range(H+2):
    for x in range(W+2):
        if S[y][x]:
            R[y][x]=R[y][x-1]+1

for y in range(H+2):
    for x in range(W+1,-1,-1):
        if S[y][x]:
            L[y][x]=L[y][x+1]+1

for x in range(W+2):
    for y in range(H+2):
        if S[y][x]:
            D[y][x]=D[y-1][x]+1

for x in range(W+2):
    for y in range(H+1,-1,-1):
        if S[y][x]:
            U[y][x]=U[y+1][x]+1

A=[[0]*(W+2) for _ in range(H+2)]
for y in range(H+2):
    for x in range(W+2):
        A[y][x]=U[y][x]+D[y][x]+R[y][x]+L[y][x]-3

M=0
for y in range(H+2):
    M=max(M,max(A[y]))

print(M)