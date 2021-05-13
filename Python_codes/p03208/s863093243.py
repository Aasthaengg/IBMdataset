def resolve():
    N, K = [int(i) for i in input().split()]
    H = sorted([int(input()) for _ in range(N)])
    minA = float("inf")
    for i in range(N - K + 1):
        minA = min(minA, H[i + K - 1] - H[i])
    print(minA)


resolve()
