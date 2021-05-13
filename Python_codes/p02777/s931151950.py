S,T = input().split()
A,B = input().split()
A = int(A)
B = int(B)
U = input()
if U == S :
    A = A - 1
    print(A,B)
elif U == T :
    B = B - 1
    print(A,B)