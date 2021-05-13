import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    if N % 2:
        print(0)
        return

    ans = N // 10
    p = 50
    while True:
        tmp = N // p
        if tmp == 0:
            break
        ans += tmp
        p *= 5

    print(ans)
    return


if __name__ == '__main__':
    main()
