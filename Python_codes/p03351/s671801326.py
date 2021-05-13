import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    a, b, c, d = map(int, readline().split())
    if abs(a-c)<=d:
        print('Yes')
    else:
        if a<=b<=c and b-a<=d and c-b<=d:
            print('Yes')
        elif c<=b<=a and b-c<=d and a-b<=d:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
