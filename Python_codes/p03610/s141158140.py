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
    s = readstr()
    l = []
    for i, x in enumerate(s):
        if not i % 2:
            l.append(x)

    print(''.join(l))


if __name__ == "__main__":
    main()
