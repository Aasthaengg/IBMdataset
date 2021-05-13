h,w=map(int,input().split())
M=[list(input()) for i in range(h)]
D=[[0]*w for i in range(h)]
U=[[0]*w for i in range(h)]
R=[[0]*w for i in range(h)]
L=[[0]*w for i in range(h)]

for i in range(h):
    c=0
    for j in range(w):
        if M[i][j]=='.':
            c+=1
            R[i][j]=c
        else:
            c=0
for i in range(h):
    c=0
    for j in range(w):
        if M[i][w-1-j]=='.':
            c+=1
            L[i][w-1-j]=c
        else:
            c=0
for j in range(w):
    c=0
    for i in range(h):
        if M[i][j]=='.':
            c+=1
            D[i][j]=c
        else:
            c=0
for j in range(w):
    c=0
    for i in range(h):
        if M[h-1-i][j]=='.':
            c+=1
            U[h-1-i][j]=c
        else:
            c=0
r=0
for i in range(h):
    for j in range(w):
        r=max(r,R[i][j]+L[i][j]+D[i][j]+U[i][j]-3)
print(r)