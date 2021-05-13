import sys


def input():
    return sys.stdin.readline().strip()
# sys.setrecursionlimit(100000)


def main():
    _ = int(input().strip())
    A = [int(i) for i in input().strip().split()]
    cnt = 0
    for a in A:
        x = a
        while x % 2 == 0:
            x = x // 2
            cnt += 1
    print(cnt)
    return


if __name__ == "__main__":
    main()
