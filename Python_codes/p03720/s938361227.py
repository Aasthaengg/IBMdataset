import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *AB = map(int, read().split())
    ans = [0] * N
    for a, b in zip(*[iter(AB)] * 2):
        ans[a - 1] += 1
        ans[b - 1] += 1

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
