def sub():
    A, B = [int(e) for e in input().split()]
    q, m = divmod(B, A)
    if q > 0 and m == 0:
        print(A+B)
    else:
        print(B-A)

sub()
