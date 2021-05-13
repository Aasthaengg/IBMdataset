import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**20
eps = 10**-7

N,K = map(int,readline().split())

P = [tuple(map(int,readline().split())) for i in range(N)]

X = []
Y = []
for (xi,yi) in P:
    X.append(xi)
    Y.append(yi)
X.sort()
Y.sort()
from itertools import combinations

ans = INF
def count(xmin,xmax,ymin,ymax):
    ret = 0
    for (xi,yi) in P:
        if (xmin <= xi <= xmax) and (ymin <= yi <= ymax):
            ret += 1
    return ret

for (xmin,xmax) in combinations(X,2):
    for (ymin,ymax) in combinations(Y,2):
        if count(xmin,xmax,ymin,ymax) >= K:
            ans = min(ans,(xmax-xmin)*(ymax-ymin))
print(ans)

