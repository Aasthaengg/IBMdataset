N=int(input())
A=[]
for i in range(1,(N//2)+1):
    A.append(list(str(i))+list(str(N-i)))
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j]=int(A[i][j])
B=[]
for i in range(len(A)):
    B.append(sum(A[i]))
print(min(B))