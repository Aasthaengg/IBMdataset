#!python3

LI = lambda: list(map(int, input().split()))

# input
N, x = LI()
A = LI()


def main():
    ans = 0
    for i in range(1, N):
        s = A[i - 1] + A[i]
        d = max(0, s - x)
        ans += d
        A[i] -= min(d, A[i])
    print(ans)


if __name__ == "__main__":
    main()
