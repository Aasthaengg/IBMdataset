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
    A = [0] + in_nl() + [0]
    N = N + 2

    dsum = 0
    for i in range(N - 1):
        dsum += abs(A[i + 1] - A[i])

    ans = [0] * (N - 2)
    for i in range(1, N - 1):
        if A[i - 1] <= A[i] and A[i] <= A[i + 1]:
            ans[i - 1] = dsum
        elif A[i - 1] >= A[i] and A[i] >= A[i + 1]:
            ans[i - 1] = dsum
        elif A[i - 1] <= A[i] and A[i] >= A[i + 1]:
            ans[i - 1] = dsum - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1])
        elif A[i - 1] >= A[i] and A[i] <= A[i + 1]:
            ans[i - 1] = dsum - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1])

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
