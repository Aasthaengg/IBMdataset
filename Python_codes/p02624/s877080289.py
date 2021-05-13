import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

n = int(readline())

cnt = [0]*(n+1)

for i in range(1,n+1):
    for j in range(i,n+1,i):
        cnt[j] += 1
ans = 0
for i in range(1,n+1):
    ans += i*cnt[i]
print(ans)
