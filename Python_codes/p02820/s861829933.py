import sys
input = sys.stdin.readline
from collections import *

def calc(l):
    dp = [[0]*3 for _ in range(len(l)+1)]
    
    for i in range(len(l)):
        dp[i+1][0] = max(dp[i][1], dp[i][2])+(R if l[i]=='s' else 0)
        dp[i+1][1] = max(dp[i][2], dp[i][0])+(S if l[i]=='p' else 0)
        dp[i+1][2] = max(dp[i][0], dp[i][1])+(P if l[i]=='r' else 0)

    return max(dp[-1])
    
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()[:-1]
d = defaultdict(list)

for i in range(N):
    d[i%K].append(T[i])

ans = 0

for i in range(K):
    ans += calc(d[i])

print(ans)