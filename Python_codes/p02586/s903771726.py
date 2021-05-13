import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

R, C, K = mapint()
last_dp = [[0]*4 for _ in range(C)]
dic = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = mapint()
    dic[r-1][c-1] = v

for r in range(R):
    dp = [[0]*4 for _ in range(C)]
    for c in range(C):
        v = dic[r][c]
        for i in range(4):
            if c!=0:
                dp[c][i] = dp[c-1][i]
            if r!=0:
                dp[c][0] = max(dp[c][0], last_dp[c][i])
        if v!=0:
            for i in range(2, -1, -1):
                dp[c][i+1] = max(dp[c][i+1], dp[c][i]+v)
    last_dp = dp

print(max(dp[C-1]))