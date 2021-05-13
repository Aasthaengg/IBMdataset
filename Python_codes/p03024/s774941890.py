import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = readline().decode('utf-8').strip()
    if S.count('o') + (15-len(S)) >= 8:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
