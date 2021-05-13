import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    r, D, x = map(int, readline().split())
    for _ in range(10):
        x = r * x - D
        print(x)
    
    return


if __name__ == '__main__':
    main()
