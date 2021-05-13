# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))
L.sort()
ans = 10**9
for i in range(N - K+1):
    ans = min(ans, L[i+K-1]-L[i])
print(ans)
