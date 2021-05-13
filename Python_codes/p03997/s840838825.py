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
    a = readint()
    b = readint()
    h = readint()
    print((a + b) * h // 2)


if __name__ == "__main__":
    main()
