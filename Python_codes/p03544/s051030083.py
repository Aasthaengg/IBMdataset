import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
dp = [0]*90
dp[0] = 2
dp[1] = 1
for i in range(2, 90):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N])