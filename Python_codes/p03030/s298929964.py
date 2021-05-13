import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7


N = int(readline())
SP = [list(readline().split()) + [i+1] for i in range(N)]
for i in range(N):
    SP[i][1] = int(SP[i][1])
SP.sort(key=lambda x: (x[0], -x[1]))
for i in range(N):
    print(SP[i][2])