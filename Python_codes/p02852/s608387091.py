import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    S = readline().strip()

    S = S[::-1]
    idx = 0
    ans = []
    while idx < N:
        step = 0
        for i in range(min(M, N - idx), 0, -1):
            if S[idx + i] == '0':
                step = i
                break
        if step == 0:
            print(-1)
            return
        ans.append(step)
        idx += step

    print(*reversed(ans))
    return


if __name__ == '__main__':
    main()
