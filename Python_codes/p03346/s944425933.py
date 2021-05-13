def main():
    N = int(input())
    P = [int(input()) for i in range(N)]

    Q = [0]*(N+1)
    for p in P:
        Q[p] = Q[p-1] + 1
    print(N - max(Q))


if __name__ == '__main__':
    main()
