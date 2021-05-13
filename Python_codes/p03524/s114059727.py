import sys
from collections import  Counter
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7



def main():
    S = input()
    count = Counter(S)
    count['a'] += 0
    count['b'] += 0
    count['c'] += 0
    if max(count.values()) - min(count.values()) <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
