import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(1000000000)

int1 = lambda x: int(x) - 1

N, M = map(int, input().split())

not_start_point = set()
to_point = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int1, input().split())
    not_start_point.add(y)
    to_point[x].append(y)

start_point = set(range(N)) - not_start_point

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

ans = 0
for s in start_point:
    ans = max(ans, dp(s))

print(ans)