a, b, c, d = map(int,input().split())

A = a*b
B = c*d

if A>B:
    print(A)
elif B>A:
    print(B)
elif A==B:
    print(A)