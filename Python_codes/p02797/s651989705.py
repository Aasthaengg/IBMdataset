def main():
    N, K, S = (int(i) for i in input().split())
    INF = 10**9
    if S == INF:
        INF = 1
    ans = [S]*K + [INF]*(N-K)
    return print(*ans)


if __name__ == '__main__':
    main()
