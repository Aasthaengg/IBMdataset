import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    x = ans = 0
    for s in S:
        if s == 'I':
            x += 1
            if x > ans:
                ans = x
        else:
            x -= 1

    print(ans)
    return


if __name__ == '__main__':
    main()
