from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil
from bisect import bisect_left
from itertools import combinations
setrecursionlimit(100000)

INF = int(1e10)
MOD = int(1e9 + 7)

def main():
    from builtins import int, map
    N = int(input())
    AB = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        AB.append((ai, bi))
    AB = sorted(AB, key=lambda x: x[0])
    ans = AB[0][0] - 1
    for i in range(N - 1):
        diff = AB[i + 1][0] - AB[i][0]
        ans += diff
    ans += AB[-1][1] + 1
    print(ans)    

if __name__ == '__main__':
    main()
