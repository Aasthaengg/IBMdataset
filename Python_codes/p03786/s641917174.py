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
    A = sorted(in_nl())

    asum = [0] * (N + 1)
    for i in range(N):
        asum[i + 1] = asum[i] + A[i]

    ans = 1
    for i in range(N - 1, -1, -1):
        if A[i] <= asum[i] * 2:
            ans += 1
        else:
            break

    print(ans)


if __name__ == '__main__':
    main()
