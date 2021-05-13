def prime2_factorize(N):
    cnt = 0
    while N % 2 == 0:
        cnt += 1
        N //= 2
    return cnt


def resolve():
    N = int(input())
    A = [int(i) for i in input().split()]
    sumA = 0
    for a in A:
        sumA += prime2_factorize(a)
    print(sumA)


resolve()
