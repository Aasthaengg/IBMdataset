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

    for i in range(2 * H):
        print(C[i // 2])

    return


if __name__ == '__main__':
    main()
