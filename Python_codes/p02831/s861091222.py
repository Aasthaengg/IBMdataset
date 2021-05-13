from fractions import gcd
A, B = map(int, input().split())


def BIG_SMALL(A, B):
    if A % B == 0:
        print(A)
    else:
        print(A*B//gcd(A,B))


if A > B:
    BIG_SMALL(A, B)
elif A < B:
    BIG_SMALL(B, A)
else:
    print(A)
