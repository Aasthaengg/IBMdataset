import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline()
n, k = [int(i) for i in input().split()]
e = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
ans = 1
mod = 10**9+7
 
 
def dfs(i=0, r=-1):
    global ans
    if r == -1:
        ans *= k
        ans %= mod
 
        p = k-1
        for j in e[i]:
            if j == r:
                continue
            ans *= p
            ans %= mod
            p -= 1
            dfs(j, i)
    else:
        p = k-2
        for j in e[i]:
            if j == r:
                continue
            ans *= p
            ans %= mod
            p -= 1
            dfs(j, i)
 
 
dfs()
print(ans)