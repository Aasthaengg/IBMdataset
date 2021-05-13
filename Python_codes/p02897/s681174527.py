N = int(input())


if N == 1:
    print(1.0)
elif N % 2 == 0:
    print(0.5)
    exit()
elif N % 2 != 0:
    print((N - (N // 2)) / N)