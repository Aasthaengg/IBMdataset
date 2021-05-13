A=input()
N=len(A)
B=[]
C=[]
for i in range(N):
    flag=0
    for j in range(len(B)):
        if B[j]==A[i]:
            C[j]+=1
            flag=1
            break
    if flag==0:
        B.append(A[i])
        C.append(1)
M=((N*(N-1))//2)+1
for i in C:
    M -= (i*(i-1))//2
print(M)
