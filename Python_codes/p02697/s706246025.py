def main():
    N, M = map(int, input().split())

    pairs = []
    a = 1
    for d in range(M, 0, -2):
        pairs.append((a, a + d))
        a += 1

    a = 1 + M + 1
    for d in range(M - 1, 0, -2):
        pairs.append((a, a + d))
        a += 1

    for pair in pairs:
        print(*pair)


if __name__ == '__main__':
    main()
