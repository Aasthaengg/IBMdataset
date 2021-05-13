def resolve():
    N = int(input())
    A = [int(i) for i in input().split()]
    sumA = 0
    for i in range(N):
        sumA += 1 / A[i]
    print(1 / sumA)

resolve()
