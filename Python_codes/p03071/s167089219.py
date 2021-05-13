A, B = map(int,input().split())

if A == B:
    print(A+B)
elif A > B and A-1 > B:
    print(A+A-1)
elif A > B and A-1 == B:
    print(A+B)
elif A < B and A < B-1:
    print(B+B-1)
elif A < B and A == B-1:
    print(A+B)