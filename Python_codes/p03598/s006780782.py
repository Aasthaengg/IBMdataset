def solve():
    N = int(input())
    K = int(input())
    X = map(int, input().split())
    ans = 0

    for x in X:
        ans += 2 * min(K - x, x)
    print(ans)


if __name__ == "__main__":
    solve()
