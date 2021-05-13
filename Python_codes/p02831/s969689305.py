import sys
A, B = map(int, input().split())
A_, B_ = A, B
counta, countb = 1, 1
while True:
    if A == B:
        print(A)
        sys.exit()
    elif A > B:
        countb += 1
        B = B_ * countb
    elif B > A:
        counta += 1
        A = A_ * counta
