import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    N, T = readnums()
    t = list(readnums())

    ans = 0
    for i in range(N - 1):
        if t[i + 1] - t[i] >= T:
            ans += T
        else:
            ans += t[i + 1] - t[i]

    print(ans + T)


if __name__ == "__main__":
    main()
