def main():
    N, M, K = map(int, input().split())

    for n in range(N + 1):
        for m in range(M + 1):
            overlap = 2 * n * m
            cnt = n * M + m * N - overlap
            if cnt == K:
                print("Yes")
                return
    else:
        print("No")
        return


main()
