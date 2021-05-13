import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())

for i in range(1,3501):
    for j in range(1,3501):
        if 4*i*j-N*i-N*j > 0 and (N*i*j)%(4*i*j-N*i-N*j) == 0:
            print(i,j,(N*i*j)//(4*i*j-N*i-N*j))
            exit()
