import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    C = [list(map(int, readline().split())) for _ in range(3)]

    for i in range(3):
        if (
            not C[(i + 1) % 3][0] - C[i][0]
            == C[(i + 1) % 3][1] - C[i][1]
            == C[(i + 1) % 3][2] - C[i][2]
        ):
            print('No')
            return
        if (
            not C[0][(i + 1) % 3] - C[0][i]
            == C[1][(i + 1) % 3] - C[1][i]
            == C[2][(i + 1) % 3] - C[2][i]
        ):
            print('No')
            return

    print('Yes')
    return


if __name__ == '__main__':
    main()
