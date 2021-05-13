import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    A, B = map(int, readline().split())
    if A <= 5:
        print(0)
    elif A <= 12:
        print(B//2)
    else:
        print(B)
    
    return


if __name__ == '__main__':
    main()
