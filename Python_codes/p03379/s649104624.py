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
    X = in_nl()
    X = [(num, i) for i, num in enumerate(X)]

    ans = [0] * N
    X.sort()
    for i in range(N):
        _, j = X[i]
        if i < N // 2:
            ans[j] = X[N // 2][0]
        else:
            ans[j] = X[N // 2 - 1][0]

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
