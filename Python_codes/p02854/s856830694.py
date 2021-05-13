N,A=open(0)
*A,=map(int,A.split())
S=M=sum(A)
C=0
for a in A:
    C+=a
    M=min(M,abs(S-2*C))
print(M)