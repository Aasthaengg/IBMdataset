def main():
    N, K = map(int, input().split())

    snuke = [1] * N
    for _ in range(K):
        _ = int(input())
        A = (int(x) - 1 for x in input().split())
        for x in A:
            snuke[x] = 0
    print(sum(snuke))


if __name__ == '__main__':
    main()
