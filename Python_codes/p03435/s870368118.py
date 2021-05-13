A=[0]
B=[]
C=[]
for i in range(3):
    C.append(list(map(int,input().split())))
B.append(C[0][0])
B.append(C[0][1])
B.append(C[0][2])
A.append(C[1][0]-B[0])
A.append(C[2][0]-B[0])
for i in range(3):
    for j in range(3):
            if(C[i][j]!=A[i]+B[j] and C[i][j]!=B[i]+A[j]):
                print('No')
                exit()
print('Yes')