import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    n = readline().strip()
    print(n.translate(n.maketrans('19', '91')))

    return


if __name__ == '__main__':
    main()
