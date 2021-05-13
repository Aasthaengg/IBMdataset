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
	
n,k = gil()
h = gil()

dp = [1e18] * n
dp[0] = 0
for i in range(n):
    for j in range(i+1, i+k+1):
        if j < n:
            dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j]))
#print(dp)
print(dp[n-1])
# Each iteration will consider the following for a state ->
# 1. Does this path get the min cost for this end point (each iteration is treated as
#       an endpoint), when considering the cost for this jump + the cost baggage
#       that this path brings. so that is dp[upto_here] + jump_cost or existing dp[endpoint] 
#       from some previous state.
# 2. Each iteration on i will try to cover all the possible states reachable,
#       while trying to set the min value for each state, as in, see if this state
#       is the best one so far.