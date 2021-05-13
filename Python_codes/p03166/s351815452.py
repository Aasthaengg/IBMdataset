import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(1000000000)

int1 = lambda x: int(x) - 1

N, M = map(int, input().split())

to_point = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int1, input().split())
    to_point[x].append(y)

dp_memo = [-1]*N
for x in range(N):
    if len(to_point[x]) == 0:
        dp_memo[x] = 0

# 点i始点のLongest Pathの長さ
def dp(i):
    if dp_memo[i] >= 0:
        return dp_memo[i]
    lp = 0
    for j in to_point[i]:
        lp = max(lp, dp(j)+1)
    dp_memo[i] = lp
    return lp

for i in range(N):
    dp(i)

print(max(dp_memo))