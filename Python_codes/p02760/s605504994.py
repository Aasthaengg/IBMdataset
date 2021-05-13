A=[]
B=[]
for i in range(3):
    A.append(list(map(int,input().split())))
N=int(input())
for i in range(N):
    B.append(int(input()))
for i in range(3):
    for j in range(3):
        for k in range(N):
            if A[i][j]==B[k]:
                A[i][j]=-1
C=[]
for i in range(3):
    if A[0][0]==A[1][1] and A[1][1]==A[2][2] and A[2][2]==-1:
        C.append('Yes')
    elif A[0][2]==A[1][1] and A[1][1]==A[2][0] and A[2][0]==-1:
        C.append('Yes')
    elif A[i][0]==A[i][1] and A[i][1]==A[i][2]:
        C.append('Yes')
    elif A[0][i]==A[1][i] and A[1][i]==A[2][i]:
        C.append('Yes')
    else:
        C.append('No')
if 'Yes' in C:
    print('Yes')
else:
    print('No')