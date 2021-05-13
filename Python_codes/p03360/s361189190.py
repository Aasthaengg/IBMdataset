import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A = list(map(int, readline().split()))
    K = int(readline())

    A.sort()
    for _ in range(K):
        A[-1] *= 2

    print(sum(A))

    return


if __name__ == '__main__':
    main()
