# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
D, X = map(int, input().split())
list_A = [int(input()) for i in range(N)]
list_n = [0] * N

for i in range(1, D + 1):
    for j in range(N):
        if (i - 1) % list_A[j] == 0:
            list_n[j] += 1
print(sum(list_n)+X)
