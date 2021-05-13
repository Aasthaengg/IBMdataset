import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X, A, B = map(int, readline().split())
    if -A+B<=0:
        print('delicious')
    elif 0<-A+B<=X:
        print('safe')
    else:
        print('dangerous')


if __name__ == '__main__':
    main()
