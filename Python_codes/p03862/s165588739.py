import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, X = in_nn()
    A = in_nl()

    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
            A[i] = X

    for i in range(1, N):
        if A[i - 1] + A[i] > X:
            ans += A[i] - (X - A[i - 1])
            A[i] = X - A[i - 1]

    # print(A)
    print(ans)


if __name__ == '__main__':
    main()
