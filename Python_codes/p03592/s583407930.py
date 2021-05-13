def main2():
    N, M, K = map(int, input().split())

    for i in range(N + 1):
        for j in range(M + 1):
            b = i * (M - j) + j * (N - i)

            if b == K:
                print("Yes")
                exit()

    print("No")

if __name__ == "__main__":
    main2()