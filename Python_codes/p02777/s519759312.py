S, T = map(str, input().split())
A, B = map(int, input().split())
U = str(input())

if S == U:
    A -= 1
    print(A,B)

elif T == U:
    B -= 1
    print(A,B)