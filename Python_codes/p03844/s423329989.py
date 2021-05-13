import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, op, B = readline().split()
    A, B = int(A), int(B)
    if op == '+':
        print(A + B)
    else:
        print(A - B)

    return


if __name__ == '__main__':
    main()
