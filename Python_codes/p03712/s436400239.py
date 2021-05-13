import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    ans = [0] * (H + 2)
    ans[0] = '#' * (W + 2)
    for i in range(1, H + 1):
        ans[i] = '#' + readline().strip() + '#'
    ans[H + 1] = '#' * (W + 2)

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
