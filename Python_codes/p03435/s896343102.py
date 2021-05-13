import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    C = [list(map(int, readline().split())) for _ in range(3)]

    A = [0] * 3
    B = [0] * 3

    for i in range(3):
        B[i] = C[0][i]

    for i in range(1, 3):
        A[i] = C[i][0] - B[0]

    for i in range(3):
        for j in range(3):
            if C[i][j] != A[i] + B[j]:
                print('No')
                return

    print('Yes')
    return


if __name__ == '__main__':
    main()
