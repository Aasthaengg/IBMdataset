num=list(map(int,input().split(" ")))
A=[list(map(int,input().split(" ")))for i in range(num[0])]
B=[list(map(int,input().split(" ")))for i in range(num[1])]
C=[[0]*num[2] for i in range(num[0])]

for i in range(num[0]):
    for j in range(num[2]):
        for k in range(num[1]):
            C[i][j]+=A[i][k]*B[k][j]
for i in C:
    print(" ".join(map(str,i)))
