import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b, c = map(int, readline().split())
    print(a+b+c-max(a,b,c))


if __name__ == '__main__':
    main()
