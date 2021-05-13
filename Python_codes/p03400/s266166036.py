def resolve():
    N = int(input())
    D, X = [int(i) for i in input().split()]
    A = [int(input()) for _ in range(N)]
    for a in A:
        X += -(-D // a)
    print(X)

resolve()
