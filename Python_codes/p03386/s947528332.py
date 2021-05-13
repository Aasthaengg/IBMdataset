def resolve():
    A, B, K = list(map(int, input().split()))
    if B - A + 1 >= 2 * K:
        ls = [i for i in range(A, A+K)] + [i for i in range(B-K+1, B+1)]
    else:
        ls = [i for i in range(A, B+1)]

    print('\n'.join(map(str, ls)))
    return

resolve()