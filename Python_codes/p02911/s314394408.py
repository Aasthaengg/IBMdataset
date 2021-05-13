X = list(map(int, input().split()))
A = []
B=[]
C=[]
for _ in range(X[2]):
    A.append(int(input()))
for _ in range(X[0]):
    B.append(X[1]-X[2])
for i in range(0,X[2]):
    B[A[i]-1]=B[A[i]-1]+1
for j in range(0,X[0]):
    if B[j]>0:
        C.append("Yes")
    else:
        C.append("No")
[print(i) for i in C]

# 難しかった