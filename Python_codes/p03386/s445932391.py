A,B,K=map(int,input().split())
C=[]
D=[]
for i in range(K):
    if A+i<=B:
        C.append(A+i)
for i in range(K):
    if B-i>=A:
        D.append(B-i)
E=C+D
E.sort()
F=list(set(E))
F.sort()
for i in range(len(F)):
    print(F[i])