# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())
list_P = [K-Q] * N
for i in range(Q):
    A = int(input())
    list_P[A-1] += 1

for i in range(N):
    if list_P[i] <= 0:
        print("No")
    else:
        print("Yes")
