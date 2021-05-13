import math

n=int(input())
L=list(input().split())
M=list(input().split())

A=0
B=0
D=0
N=[]

for i in range(n):
    a=float(L[i])
    b=float(M[i])
    
    if a>b:
        A+=a-b
        D+=(a-b)**3
        N.append(a-b)
    else:
        A+=b-a
        D+=(b-a)**3
        N.append(b-a)
        
    B+=(a-b)**2
    C=math.sqrt(B)
    
    E=D**(1/3)

print(A)
print(C)
print(E)
print(max(N))
