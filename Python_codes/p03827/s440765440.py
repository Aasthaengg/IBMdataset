# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N = int(input())
S = input()

ans = 0
x = 0
for i in range(len(S)):
    if S[i] == "I":
        x += 1
    else:
        x -= 1
    ans = max(ans, x)

print(ans)
