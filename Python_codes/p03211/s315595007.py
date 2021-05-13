# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = input()
ans = 999
for i in range(len(S) - 3):
    ans = min(abs(int(S[i:i+3])-753), ans)
print(ans)
