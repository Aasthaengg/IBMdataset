def resolve():
    N = int(input())
    A = [int(i) for i in input().split()]
    cumsumA = [0] * (N + 1)
    cumsumB = [0] * (N + 1)
    for i in range(N):
        cumsumA[i + 1] = cumsumA[i] + A[i]
        cumsumB[N - i - 1] = cumsumB[N - i] + A[N - i - 1]
    minA = 10**18
    for i in range(N + 1):
        minA = min(minA, abs(cumsumA[i] - cumsumB[i]))
    print(minA)


resolve()
