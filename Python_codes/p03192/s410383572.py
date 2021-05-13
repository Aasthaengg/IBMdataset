import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = readline().decode('utf-8').strip()
    print(N.count('2'))

if __name__ == '__main__':
    main()
