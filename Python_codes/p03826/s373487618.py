A,B,C,D = [int(i) for i in input().split()]

S1 = int(A*B)
S2 = int(C*D)

if S1 >= S2:
    print(S1)
elif S2 > S1:
    print(S2)
