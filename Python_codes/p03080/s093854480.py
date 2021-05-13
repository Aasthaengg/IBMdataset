import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    S = readline().decode('utf-8').strip()
    red = S.count('R')
    if red>N-red:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
