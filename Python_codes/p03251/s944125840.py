import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M, X, Y = map(int, readline().split())
    x_max = max(list(map(int, readline().split())))
    y_min = min(list(map(int, readline().split())))
    if max(X,x_max)<min(Y,y_min):
        print('No War')
    else:
        print('War')



if __name__ == '__main__':
    main()
