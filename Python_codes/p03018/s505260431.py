import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def t(S):

    N = len(S)

    a = [0] * (N + 1)
    d = [0] * (N + 1)
    for i in range(N):
        if S[i] == 'A':
            a[i + 1] = 1
        else:
            d[i + 1] = 1

    for i in range(N):
        a[i + 1] += a[i]
        d[i + 1] += d[i]

    ans = 0
    for i in range(1, N):
        if S[i] == 'D':
            ans += a[i]

    return ans


def main():

    S = in_s()
    S = S.replace('BC', 'D')
    S = S.replace('B', ' ')
    S = S.replace('C', ' ')

    ans = 0
    for ts in S.split():
        ans += t(ts)

    print(ans)


if __name__ == '__main__':
    main()
