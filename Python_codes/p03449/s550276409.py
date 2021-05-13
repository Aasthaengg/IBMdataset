import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    A = list(accumulate(A))
    B = list(accumulate(B))

    ans = 0
    for i in range(N):
        if i > 0:
            res = A[i] + B[-1] - B[i - 1]
        else:
            res = A[i] + B[-1]

        if ans < res:
            ans = res

    print(ans)

    return


if __name__ == '__main__':
    main()
