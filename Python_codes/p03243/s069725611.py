import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    while True:
        if len(set(str(N))) == 1:
            print(N)
            break
        else:
            N += 1


if __name__ == '__main__':
    main()
