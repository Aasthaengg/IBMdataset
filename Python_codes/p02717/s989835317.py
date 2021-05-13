X,Y,Z=map(int,input().split())
A=X
B=Y
C=Z
A,B=B,A
A,C=C,A
print(A,B,C)