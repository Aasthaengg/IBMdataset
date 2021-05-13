import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))

    A.sort()

    ans = (A[2] - A[0]) // 2 + (A[2] - A[1]) // 2
    A[0] += (A[2] - A[0]) // 2 * 2
    A[1] += (A[2] - A[1]) // 2 * 2

    if A[0] == A[1]:
        if A[0] < A[2]:
            ans += 1
    else:
        ans += 2

    print(ans)
    return


if __name__ == '__main__':
    main()
