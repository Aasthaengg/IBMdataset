import sys
import re

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input()
    if re.fullmatch('A?KIHA?BA?RA?', S):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
