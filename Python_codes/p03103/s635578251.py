# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = []
for i in range(N):
    a, b = map(int, input().split())
    L.append((a, b))
L = sorted(L, key=lambda x: x[0])

n = 0
ans = 0
for i in range(N):
    if n + L[i][1] <= M:
        ans += L[i][1] * L[i][0]
        n += L[i][1]
    else:
        ans += (M-n) * L[i][0]
        n = M
        break
print(ans)
