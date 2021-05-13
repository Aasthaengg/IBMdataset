import sys

input = sys.stdin.readline


# Editorial AC
def main():
    M, K = map(int, input().split())

    if K >= 2 ** M:
        print(-1)
        exit()

    if M == 1:
        if K == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
        exit()

    A = list(range(2 ** M))
    B = list(reversed(range(2 ** M)))
    A.remove(K)
    B.remove(K)

    ans = A + [K] + B + [K]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
