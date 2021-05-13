import sys
I = lambda:map(int,sys.stdin.readline().split())
pr = lambda x:sys.stdout.write(f'{x}\n')
sys.setrecursionlimit(2000000001)

mn = lambda w,x,y,z: min(abs(w)+x,abs(y)+z)
n = ar = dp = 0

def solve(x):
	global n,ar,dp
	if x>=n-2: return dp[x]
	if dp[x] != -1: return dp[x]
	dp[x] = mn(ar[x]-ar[x+1], solve(x+1), ar[x]-ar[x+2], solve(x+2))
	# pr(f'{x} => {dp[x]}')
	return dp[x]

def main():
	global n,ar,dp
	n, ar = *I(), [*I()]
	dp = [-1]*(n-2) + [abs(ar[-2]-ar[-1]),0]
	# pr((n,ar,dp))
	pr(solve(0))

main()