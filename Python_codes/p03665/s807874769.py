def m():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    Even = [a for a in A if a % 2 == 0]
    Odd = [a for a in A if a % 2 == 1]
    if P == 1 and len(Odd) == 0:
        return 0

    if len(Odd) == 0:
        return pow(2, len(Even))
    else:
        return pow(2, N-1)


print(m())
