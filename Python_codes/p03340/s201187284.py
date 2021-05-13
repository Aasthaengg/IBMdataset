import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    s = 0
    xors = 0
    ans = 0
    right = 0
    for left in range(N):
        while right < N and xors ^ A[right] == s + A[right]:
            xors ^= A[right]
            s += A[right]
            right += 1

        ans += right - left

        if left == right:
            right += 1
        else:
            xors ^= A[left]
            s -= A[left]

    print(ans)
    return


if __name__ == '__main__':
    main()
