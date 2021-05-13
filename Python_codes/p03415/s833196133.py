import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    C = [readline().strip() for _ in range(3)]

    print(C[0][0] + C[1][1] + C[2][2])

    return


if __name__ == '__main__':
    main()
