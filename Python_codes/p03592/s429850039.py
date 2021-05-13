import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N,M,K = map(int,readline().split())

for i in range(N+1):
    for j in range(M+1):
        if i*j+(N-i)*(M-j) == K:
            print('Yes')
            exit()
print('No')