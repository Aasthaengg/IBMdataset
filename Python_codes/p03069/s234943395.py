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
    S = list(in_s())[::-1]

    cb = [0] * (N + 1)
    cw = [0] * (N + 1)
    for i in range(N):
        if S[i] == '#':
            cb[i + 1] = 1
        else:
            cw[i + 1] = 1

    for i in range(N):
        cb[i + 1] += cb[i]
        cw[i + 1] += cw[i]

    ans = S.count('.')
    for i in range(N + 1):
        ans = min(ans, cw[i] + cb[N] - cb[i])

    print(ans)


if __name__ == '__main__':
    main()
