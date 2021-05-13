import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a) / n
    c = [abs(b - a[i]) for i in range(n)]
    print(c.index(min(c)))


if __name__ == '__main__':
    main()
