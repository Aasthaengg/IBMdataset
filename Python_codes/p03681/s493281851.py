def main():
    MOD = 10 ** 9 + 7

    N, M = map(int, input().split())
    if abs(N - M) > 1:
        print(0)
        return

    ans = 1
    for i in range(1, N + 1):
        ans = (ans * i) % MOD

    for i in range(1, M + 1):
        ans = (ans * i) % MOD

    if N == M:
        ans = (ans * 2) % MOD

    print(ans)


if __name__ == '__main__':
    main()
