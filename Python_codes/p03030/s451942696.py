# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    c, p = input().split()
    p = int(p)
    L.append([i+1, c, p])
L = sorted(L, key=lambda x: (x[1], -x[2]))
for i in range(N):
    print(L[i][0])
