import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (*A,) = map(int, read().split())

    ans = INF
    for i in range(5):
        res = A[i]
        for j in range(5):
            if j != i:
                res += (A[j] + 9) // 10 * 10
        if ans > res:
            ans = res

    print(ans)
    return


if __name__ == '__main__':
    main()
