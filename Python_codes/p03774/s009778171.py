import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(N)]
    CD = [list(map(int, readline().split())) for _ in range(M)]

    ans = [0] * N
    for i, (a, b) in enumerate(AB):
        dist = INF
        for j, (c, d) in enumerate(CD):
            if dist > abs(a - c) + abs(b - d):
                dist = abs(a - c) + abs(b - d)
                res = j
        ans[i] = res + 1

    print(*ans, sep='\n')
    return


if __name__ == '__main__':
    main()
