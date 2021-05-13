import sys
from functools import reduce
sys.setrecursionlimit(2000000001)

def solve(n,k,ar,dp,x):
	ab = abs; mn = min
	if x>=n-2: return dp[x]
	if not dp[x] is -1: return dp[x]
	# t = [ for i in range(x+1,mn(n,x+k+1))]
	t = map(lambda i:ab(ar[x]-ar[i])+solve(n,k,ar,dp,i), range(x+1,mn(n,x+k+1)))
	dp[x] = reduce(lambda a,b : a if a < b else b,t)
	return dp[x]

def main():
	I = lambda:map(int,sys.stdin.readline().split())
	pr = lambda x:sys.stdout.write(f'{x}\n')
	n,k, ar = *I(), [*I()]
	dp = [-1]*(n-2) + [abs(ar[-2]-ar[-1]),0]
	pr(solve(n,k,ar,dp,0))

main()