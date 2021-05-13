import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    D, T, S = map(int, readline().split())
    
    if D / S <= T:
        print('Yes')
    else:
        print('No')
    
    return


if __name__ == '__main__':
    main()
