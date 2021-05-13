def solve():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 13
    for r, l in zip(x[:N - K + 1], x[K - 1:]):
        ans = min(ans, abs(l) + abs(r - l), abs(r) + abs(r - l))

    print(ans)


if __name__ == "__main__":
    solve()
