A,B,C,D=input().split()
A=int(A)
B=int(B)
C=int(C)
D=int(D)

sumL=A+B
sumR=C+D


if sumL>sumR:
    print('Left')
elif sumL<sumR:
    print('Right')
else:
    print('Balanced')