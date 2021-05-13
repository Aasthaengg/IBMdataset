N = int(input())
if N % 2 == 1:
    M = int(((N - 1) ** 2 // 2))
    print(M)
    for i in range(1, N):
        print(i, N)
    for i in range(1, int((N - 1) / 2) + 1):
        for j in range(i + 1, N):
            if i + j < N:
                print(i, j)
                print(j, N - i)

else:
    M = int(N * (N - 2) // 2)
    print(M)
    for i in range(N - 2):
        print(1, i + 2)
        print(i + 2, N)
    for i in range(2, int(N / 2) + 1):
        for j in range(i + 1, N):
            if i + j < N + 1:
                print(i, j)
                print(j, N + 1 - i)