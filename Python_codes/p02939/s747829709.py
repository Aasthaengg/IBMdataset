# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

S = input().rstrip('\n')
left = ''
now = ''
ans = 0
for i in range(len(S)):
    now += S[i]
    if left != now:
        ans += 1
        left = now
        now = ''
    # print(S[i], ans)
print(ans)
