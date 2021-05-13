S,T = input().split()
A,B = map(int,input().split())
U = input()
if U == S:
    print(A - 1,end=" ")
    print(B)
else:
    print(A,end=" ")
    print(B - 1)