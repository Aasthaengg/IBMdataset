def resolve():
    A, B, C, K = list(map(int, input().split()))

    if A >= K:
        print(K)
        return
    if A + B >= K:
        print(A)
        return

    print(A-(K - A - B))

    return


resolve()