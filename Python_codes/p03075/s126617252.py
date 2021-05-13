A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
Q=int(input())
F=A-B
G=A-C
H=A-D
I=A-E
J=B-C
K=B-D
L=B-E
M=C-D
N=C-E
O=D-E

P=max(abs(F),abs(G),abs(H),abs(I),abs(J),abs(K),abs(L),abs(M),abs(N),abs(O))
if P<=Q:
    print("Yay!")
else:
    print(":(")