# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
Hn = list(map(int, input().split()))

ans = 0
n = 0
for i in range(1, N):
    b = Hn[i] - Hn[i-1]
    if b <= 0:
        n += 1
    else:
        ans = max(ans, n)
        n = 0
    if i == N - 1:
        ans = max(ans, n)
print(ans)
