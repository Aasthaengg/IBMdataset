import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    R = int(readline())
    G = int(readline())
    ans = 2*(G-R)+R
    print(ans)


if __name__ == '__main__':
    main()
