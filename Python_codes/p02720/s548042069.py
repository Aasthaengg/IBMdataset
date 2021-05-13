def f(k):
    import itertools

    N = [[str(i) for i in range(10)]]
    n = 0
    while n < k:
        T = []
        U = [n[0] for n in N[-1]]
        anchor = 0
        for i in range(len(U) - 1):
            if U[i] != U[i + 1]:
                T.append((anchor, i + 1))
                anchor = i + 1
        else:
            T.append((anchor, len(U)))
        M = []
        for i in range(10):
            for d in (-1, 0, 1):
                if 0 <= i + d < len(T):
                    for j in range(*T[i + d]):
                        M.append("{}{}".format(i, N[-1][j]))
        N[-1] = [n for n in N[-1] if not n.startswith("0")]
        n += len(N[-1])
        N.append(M)
    N = list(itertools.chain.from_iterable(N))
    return N[k - 1]


K = int(input())
print(f(K))
