import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W = map(int, readline().split())
    C = [readline().strip() for _ in range(H)]

    ans = [0] * (2 * H)
    for i in range(2 * H):
        ans[i] = C[i // 2]

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
