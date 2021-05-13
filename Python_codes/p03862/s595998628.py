import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, x, *A = map(int, read().split())

    if A[0] > x:
        ans1 = A[0] - x
        prev = x
    else:
        ans1 = 0
        prev = A[0]
    for i in range(1, N):
        if prev + A[i] > x:
            ans1 += prev + A[i] - x
            prev = x - prev
        else:
            prev = A[i]

    if A[-1] > x:
        ans2 = A[-1] - x
        prev = x
    else:
        ans2 = 0
        prev = A[-1]
    for i in range(N - 2, -1, -1):
        if prev + A[i] > x:
            ans2 += prev + A[i] - x
            prev = x - prev
        else:
            prev = A[i]

    print(min(ans1, ans2))
    return


if __name__ == '__main__':
    main()
