
ans = float("inf")


def solve():

    N, K = map(int, input().split())

    if N % K:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    solve()
