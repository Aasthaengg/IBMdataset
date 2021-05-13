import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    ans = int(N ** 0.5) ** 2
    print(ans)


if __name__ == '__main__':
    main()
