N=int(input())
SP=[]
for i in range(N):
    SP.append(list(input().split()))
for i in range(N):
    SP[i].append(i+1)
A=[]
B=[]
C=[]
for i in range(N):
    A.append(SP[i][0])
A.sort()
B.append(A[0])
for i in range(0,N-1):
    if A[i]!=A[i+1]:
        B.append(A[i+1])
for i in range(len(B)):
    C.append([])
for i in range(len(B)):
    for j in range(len(SP)):
        if B[i]==SP[j][0]:
            C[i].append([int(SP[j][1]),SP[j][2]])
for i in range(len(C)):
    for j in range(1,len(C[i])):
        d=C[i][j]
        k=j-1
        while (k>=0 and C[i][k]<d):
            C[i][k+1]=C[i][k]
            k-=1
        C[i][k+1]=d
for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j][1])