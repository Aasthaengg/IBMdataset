def resolve():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    ans = 0
    diff = []
    for i in range(M):
        P, X = list(map(int, input().split()))
        print(sum(T) - T[P-1] + X)

    return

resolve()