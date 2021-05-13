import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    S = in_s()

    wsum = [0] * N

    for i in range(N):
        if S[i] == 'W':
            wsum[i] += 1

    for i in range(N - 1):
        wsum[i + 1] += wsum[i]

    ans = 10**9 + 7
    for i in range(N):
        t = N - (i + 1) - (wsum[N - 1] - wsum[i])
        if i != 0:
            t += wsum[i - 1]
        ans = min(ans, t)

    print(ans)


if __name__ == '__main__':
    main()
