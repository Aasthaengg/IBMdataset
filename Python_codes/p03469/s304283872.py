import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    S = S.replace('2017','2018')
    print(S)


if __name__ == '__main__':
    main()
