from collections import defaultdict, Counter
import sys
sys.setrecursionlimit(10 ** 9)
def solve(num):
    #base case:
    if(dic[num]==0):
        return 0

    mx = 0
    for el in dic[num]:
        if(dp[el]==-1):
            temp1 = solve(el)
            mx = max(mx, 1 + temp1)
            dp[el] = temp1
        else:
            mx = max(mx, 1 + dp[el])

    return mx

n, m = map(int, input().split())
dic = defaultdict(int)

for _ in range(m):
    xtemp, ytemp = map(int, input().split())
    if(xtemp not in dic):
        dic[xtemp] = []
        dic[xtemp].append(ytemp)
    else:
        dic[xtemp].append(ytemp)
#init dp:
dp = [-1]*(n+1)

mxGl = 0
keys = list(dic.keys())
for node in keys:
    if(dp[node]==-1):
        temp = solve(node)
        dp[node] = temp
        mxGl = max(mxGl, temp)
    else:
        mxGl = max(mxGl, dp[node])
print(mxGl)