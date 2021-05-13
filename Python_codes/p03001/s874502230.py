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
    W, H, x, y = readnums()
    ans = W * H / 2
    if x == W / 2 and y == H / 2:
        print(ans, 1)
    else:
        print(ans, 0)


if __name__ == "__main__":
    main()
