import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,M,K = MI()
a = sum(K == i*(M-j)+j*(N-i) for i in range(N+1) for j in range(M+1))
print('Yes' if a != 0 else 'No')
