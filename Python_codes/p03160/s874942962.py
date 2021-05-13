from sys import stdin,stdout,setrecursionlimit
from collections import Counter as C
setrecursionlimit(10**6)
M = 1000000007
input = stdin.readline
def write(n,sep="\n"):
	stdout.write(str(n))
	stdout.write(sep)
def gil():
	return list(map(int, input().split()))
	
n = int(input())
h = gil()
dp = [1e18]*(n+1)
dp[0] = 0
for i in range(n):
    for j in [i+1, i+2]:
        if j < n:
            dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))
print(dp[n-1])
