
def resolve():
    A, B, C = list(map(int,input().split()))
    if A == B:
        print(C)
    if B == C:
        print(A)
    if C == A:
        print(B)


if '__main__' == __name__:
    resolve()