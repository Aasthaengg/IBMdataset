def ri():
    return int(input())


def rii():
    return [int(v) for v in input().split()]


def solve():
    N = ri()
    ans = 0
    for a in range(1, N):
        b = 1
        while b * a < N:
            ans += 1
            b += 1
    print(ans)


if __name__ == "__main__":
    solve()