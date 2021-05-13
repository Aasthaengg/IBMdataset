def resolve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    a, b = None, None
    import itertools
    for i, vars in enumerate(itertools.permutations(range(1, N+1))):
        if a is None:
            for j in range(N):
                if vars[j] != P[j]:
                    break
            else:
                a = i
        if b is None:
            for j in range(N):
                if vars[j] != Q[j]:
                    break
            else:
                b = i
        if a is not None and b is not None:
            break
    print(abs(a-b))


if '__main__' == __name__:
    resolve()