A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if A*B>C*D:
    print(A*B)
elif C*D>A*B:
    print(C*D)
elif A*B==C*D:
    print(A*B)