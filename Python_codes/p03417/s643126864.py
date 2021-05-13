N, M = map(int, input().split())

if N >= 3 and M >= 3:
    print((N - 2) * (M - 2))
elif N == 2 or M == 2:
    print(0)
elif N == 1 and M == 1:
    print(1)
elif N == 1 or M == 1:
    print(N*M - 2)