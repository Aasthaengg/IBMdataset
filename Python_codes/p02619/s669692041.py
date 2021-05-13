import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

D = int(readline())
C = list(map(int,readline().split()))
S = [list(map(int,readline().split())) for i in range(D)]
t = [int(readline()) for i in range(D)]

ans = 0
minus = 0
last = [0]*26
for i in range(D):
    ans += S[i][t[i]-1]
    minus = 0
    last[t[i]-1] = i+1
    for j in range(26):
        minus += C[j]*(i-last[j]+1)
    ans -= minus
    print(ans)

