N, M = map(int, input().split(' '))

if N == 1 and M == 1:
    print(1)
elif N == 1 or M == 1:
    print(max(0, M * N - 2))
else:
    print(max(0, N * M - (2 * (N + M - 2))))
