N=int(input())
A=input()
B=input()
C=input()


M=0
for i in range(N):
    a=len(set([A[i],B[i],C[i]]))
    if a==2:
        M+=1
    elif a==1:
        M+=0
    elif a==3:
        M+=2
print(M)