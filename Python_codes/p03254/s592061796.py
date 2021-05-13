# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, x = map(int, input().split())
list_N = list(map(int, input().split()))
list_N.sort()

list_sum = [0]
for i in range(N):
    list_sum.append(list_sum[i] + list_N[i])

ans = 0
for i in range(N + 1):
    if list_sum[i] <= x and i < N:
        ans = i
    elif i == N and list_sum[i] == x:
        ans = i


print(ans)
