import sys
sys.setrecursionlimit(2000000001)
n,ar,dp = 0,0,0

def solve(d,pi):
	global n,ar,dp
	if d>=n: return 0
	if dp[d][pi]:
		# print(f'final day=>({dp[d][pi]}),{d},prev = {pi}')
		return dp[d][pi]

	# print('day = ',d,';','prev job = ',pi,';')	##########################################
	# print('j=',[j for j in range(3) if not j is pi])	##############

	m = 0
	for j in range(3):
		if not j is pi:
			tmp = solve(d+1,j)
			# print('tmp=',ar[d][j], '+', tmp,'; d=',d,';pi=',pi)
			m = max(m,ar[d][pi] + tmp)
	# tmp = [ar[d][j] + solve(d+1,j) for j in range(3) if not j is pi]
	dp[d][pi] = m	#max(tmp)

	# print('m=',m)	##############################################
	# for i in range(n):print(dp[i])	##################################
	# print('-----')		##############################################

	return dp[d][pi]

def main():
	global n,ar,dp
	I = lambda:map(int,sys.stdin.readline().split())
	pr = lambda x:sys.stdout.write(f'{x}\n')
	n, = I()
	ar = [[*I()] for _ in range(n)]
	dp = [[0,0,0] for _ in range(n-1)]+[ar[-1]]
	pr(max(solve(0,0),solve(0,1),solve(0,2)))
	# pr('')
	# for i in range(n):print(dp[i])

main()