n,m,l = map(int,(input().split()))
A=[]
B=[]
C=[]
cc=[]
x=0
for i in range(n):
    k = [int(i) for i in input().split()]
    A.append(k)

for i in range(m):
    k = [int(i) for i in input().split()]
    B.append(k)




for i in range(n):
    for j in range(l):
        for k in range(m):
            x += A[i][k]*B[k][j]
        cc.append(x)
        x=0
    C.append(cc)
    cc=[]

for j in C:
    print(' '.join(map(str, j)))