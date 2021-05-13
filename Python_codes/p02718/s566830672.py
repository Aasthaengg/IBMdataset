import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, *A = map(int, read().split())

    A.sort(reverse=True)
    
    if A[M - 1] >= sum(A) / (4 * M):
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
