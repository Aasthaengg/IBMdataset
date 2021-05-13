def resolve():
    N = int(input())
    K = int(input())
    X = [int(i) for i in input().split()]
    sumA = 0
    for i in range(N):
        sumA += min(X[i] * 2, abs(K - X[i]) * 2)
    print(sumA)


resolve()
