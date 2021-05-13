import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    W, H, x, y = map(int, readline().split())

    ans = [W * H / 2]

    if W == 2 * x and H == 2 * y:
        ans.append(1)
    else:
        ans.append(0)

    print(*ans)
    return


if __name__ == '__main__':
    main()
