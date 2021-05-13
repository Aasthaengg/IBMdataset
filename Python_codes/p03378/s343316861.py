# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
list_A = list(map(int, input().split()))
l = 0
r = 0

for A in list_A:
    if A < X:
        l += 1
    else:
        r += 1

print(min(l, r))
