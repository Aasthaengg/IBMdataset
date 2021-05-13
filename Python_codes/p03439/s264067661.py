import sys
from collections import defaultdict
from heapq import *
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, M, = map(int, input().split())
N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# S = input().strip

x = 0
y = N

p = [None] * N
print(x, flush = True)
p[x] = input().strip()

for _ in range(20):
    m = (x + y) // 2
    print(m, flush = True)

    s = input().strip()
    if s == "Vacant":
        exit()
    else:
        if p[x] == s:
            if (m - x) % 2 == 0:
                x = m
                p[x] = s
            else:
                y = m
                p[y] = s
        else:
            if (m - x) % 2 == 0:
                y = m
                p[y] = s
            else:
                x = m
                p[x] = s