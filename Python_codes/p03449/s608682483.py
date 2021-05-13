def resolve():
    N = int(input())
    A1 = [int(i) for i in input().split()]
    A2 = [int(i) for i in input().split()]
    maxA = 0
    for i in range(N + 1):
        maxA = max(maxA, sum(A1[:i + 1]) + sum(A2[i:]))
    print(maxA)


resolve()
