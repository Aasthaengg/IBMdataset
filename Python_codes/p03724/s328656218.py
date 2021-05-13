import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N, M = map(int, readline().split())
    d = defaultdict(int)
    for _ in range(M):
        a, b = map(int, readline().split())
        d[a] += 1
        d[b] += 1
    for i in d.values():
        if i%2==1:
            print('NO')
            break
        else:
            continue
    else:
        print('YES')

if __name__ == '__main__':
    main()