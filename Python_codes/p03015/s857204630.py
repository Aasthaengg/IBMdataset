import sys
sys.setrecursionlimit(10**7)

l=input()
n = len(l)
mod = 10**9+7

p3 = [1]
for _ in range(len(l)+5):
    p3.append((p3[-1]*3)%mod)

def dfs(k,f):
    if k == n:
        return 1
    if not f:
        return p3[n-k]
    if l[k] == "1":
        return (dfs(k+1,False)+dfs(k+1,True)*2)%mod
    else:
        return dfs(k+1,True)%mod

print(dfs(0,True))