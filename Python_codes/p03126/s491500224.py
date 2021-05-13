import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    vec = [0] * M
    for _ in range(N):
        K, *A = map(int, readline().split())
        for a in A:
            vec[a - 1] += 1

    ans = 0
    for i, v in enumerate(vec, 1):
        if v == N:
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
