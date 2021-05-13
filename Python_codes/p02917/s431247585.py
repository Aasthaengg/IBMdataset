# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
ans = 0

ans += B[0]
for i in range(1, N - 1):
    ans += min(B[i - 1], B[i])
ans += B[N-2]

print(ans)
