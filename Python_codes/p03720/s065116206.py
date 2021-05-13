# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Load = [0 for i in range(N)]
# print(Load)

for i in range(M):
    a, b = map(int, input().split())
    Load[a-1] += 1
    Load[b-1] += 1

for i in range(N):
    print(Load[i])

# print(Load)
