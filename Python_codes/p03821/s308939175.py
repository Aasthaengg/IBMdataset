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
    N = readint()
    ab = [tuple(readnums()) for _ in range(N)]
    ans = 0
    for a, b in reversed(ab):
        ans += b - ((a + ans) % b) if (a + ans) % b else 0

    print(ans)


if __name__ == "__main__":
    main()
