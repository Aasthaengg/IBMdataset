import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    x, y = map(int, readline().split())
    if x * y >= 0:
        if x < y:
            print(y - x)
        else:
            print(x - y + 2 if x * y > 0 else x - y + 1)
    else:
        print(abs(abs(x) - abs(y)) + 1)


if __name__ == '__main__':
    main()