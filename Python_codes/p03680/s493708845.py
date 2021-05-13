import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    A = list(int(s) - 1 for s in read().split())

    ans = 0
    x = 0
    lit = [False] * N
    lit[0] = True
    while True:
        x = A[x]
        ans += 1
        if lit[x] or x == 1:
            break
        lit[x] = True

    if x != 1:
        ans = -1

    print(ans)

    return


if __name__ == '__main__':
    main()
