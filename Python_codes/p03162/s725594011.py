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
d = [0]
for i in range(n):
    d.append(gil())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for dx in range(1, n+1):
    ndp = dp[dx]
    #print(ndp)
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            ndp[i] = max(ndp[i], d[dx][i] + dp[dx-1][j])
    dp[dx] = ndp
#print(dp)
print(max(dp[-1]))

#DP tabular, setting current day dp by comparing previous days costs and finding max to
# pair current cost with prev days