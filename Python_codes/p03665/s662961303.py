def resolve():
    N, P = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    odd = 0
    for a in A:
        if a % 2 == 1:
            odd += 1
    even = N - odd
    if P == 1:
        if odd > 0:
            ans = (2**even) * (2**(odd - 1))
        else:
            ans = 0
    else:
        if odd == 0:
            ans = (2**even)
        else:
            ans = (2**even) * (2**(odd - 1))
    print(ans)


resolve()
