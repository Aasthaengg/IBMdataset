# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for i in range(0, min(A, X // 500) + 1):
    XX = X - 500 * i
    for j in range(0, min(B, XX // 100) + 1):
        XXX = XX - 100 * j
        if XXX // 50 <= C:
            ans += 1
print(ans)
