def resolve():
    N = int(input())
    A = list(reversed(sorted([int(i) for i in input().split()])))
    sumA = 0
    for i in range(N):
        sumA += A[(2 * i) + 1]
    print(sumA)


resolve()
