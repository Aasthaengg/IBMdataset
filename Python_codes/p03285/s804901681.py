import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    for i in range(0,N+1,7):
        if (N-i)%4==0:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
