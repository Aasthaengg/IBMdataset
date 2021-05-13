import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    W, a, b = map(int, readline().split())
    print(max(max(a,b)-(min(a,b)+W),0))


if __name__ == '__main__':
    main()
