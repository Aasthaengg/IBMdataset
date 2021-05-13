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
d = []
for i in range(n):
    d.append(gil())
dp = [[0,0,0]]
for dz in range(n):
    ndp = [0] * 3
    for i in range(3):
        for j in range(3):
            if i != j:
                ndp[i] = max(ndp[i], dp[dz][j] + d[dz][i])
    dp.append(ndp)
#print(dp)
print(max(dp[-1]))

    
# tabular approach
