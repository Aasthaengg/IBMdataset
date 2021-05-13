#ABC 076
N = int(input())
K = int(input())

def sousa(a, n, k):
	if(n==0): return a;
	else: return min(sousa(a*2,n-1,k), sousa(a+k,n-1,k))

print(sousa(1, N, K))