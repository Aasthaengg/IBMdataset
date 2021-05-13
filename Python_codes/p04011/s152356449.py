def resolve():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())
    if N > K:
        cost = X * K + Y * (N - K)
    else:
        cost = X * N
    print(cost)

resolve()