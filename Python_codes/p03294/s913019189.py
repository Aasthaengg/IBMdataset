def resolve():
    import math
    N = int(input())
    A = [int(i) for i in input().split()]
    lcm = A[0]
    for i in range(1, N):
        lcm = lcm * A[i] // math.gcd(lcm, A[i])
    lcm -= 1
    sumA = 0
    for a in A:
        sumA += lcm % a
    print(sumA)


resolve()
