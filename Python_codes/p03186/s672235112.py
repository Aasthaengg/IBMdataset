a=input()
A,B,C=a.split(' ')
A=int(A)
B=int(B)
C=int(C)
count=0
if A+B<C:
    print(A+2*B+1)
else:
    print(B+C)