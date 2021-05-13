def print_even_case(N):
    for i in range(1, N ):
        for j in range(i + 1, N + 1):
            if i + j != N + 1:
                print("{} {}".format(i, j))

N = int(input())

if N % 2 == 0:
    print((N - 2) * N // 2)
    print_even_case(N)
else:
    print((N - 3) * (N - 1) // 2 + (N - 1))
    print_even_case(N - 1)
    for i in range(1, N):
        print("{} {}".format(i, N))