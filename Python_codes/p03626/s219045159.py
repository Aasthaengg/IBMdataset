import sys
import math
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]
MOD = 1000000007

def main():
	N = INT()
	A = input().rstrip()
	B = input().rstrip()

	C = []
	cur = 0
	while cur < N:
		if A[cur] == B[cur]:
			C.append(1)
			cur += 1
		else:
			C.append(2)
			cur += 2
	
	if C[0] == 1: ans = 3
	else:	ans = 6
	for i in range(1, len(C)):
		if C[i] == 1 and C[i-1] == 1:
			ans *= 2
			ans %= MOD
		elif C[i] == 1 and C[i-1] == 2:
			ans *= 1
			ans %= MOD
		elif C[i] == 2 and C[i-1] == 1:
			ans *= 2
			ans %= MOD
		elif C[i] == 2 and C[i-1] == 2:
			ans *= 3
			ans %= MOD

	print(ans%MOD)

if __name__ == '__main__':
	main()