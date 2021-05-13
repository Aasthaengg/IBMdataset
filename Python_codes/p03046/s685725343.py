import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

m,k = map(int,readline().split())

if (k > 2**m-1):
    print(-1)
    exit()

if (k == 0):
    ans = [i//2 for i in range(2**(m+1))]
    print(" ".join(map(str,ans)))
    exit()

if m == 1 and k == 1:
    print(-1)
    exit()

ans = []

for i in range(2**m):
    if i != k:
        ans.append(i)
anss = [k] + ans + [k] + ans[::-1]
print(" ".join(map(str,anss)))
