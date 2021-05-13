A,B,C=map(int,input().split())
tmp1=A
A=B
B=tmp1

tmp2=A
A=C
C=tmp2

print(A,B,C)