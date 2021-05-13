import sys
sys.setrecursionlimit(10**7)
n,k = map(int,input().split())
t = [[] for _ in range(n)]
flag = [False for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    t[a-1].append(b-1)
    t[b-1].append(a-1)
res = 1
mod = 10**9+7

def dfs(s):
    global t
    global k
    global res
    global mod
    global flag
    if s == 0:
        res *= k
        tk = k-1
        for _ in range(len(t[s])):
            res *= tk
            res %= mod
            tk -= 1
    else:
        tk = k-2
        for _ in range(len(t[s])-1):
            res *= tk
            res %= mod
            tk -= 1
    flag[s] = True
    for g in t[s]:
        if not flag[g]:
            dfs(g)

if k ==1:
    if n>1:
        print(0)
    else:
        print(1)
elif k ==2:
    if n>2:
        print(0)
    else:
        print(2)
else:
    dfs(0)
    print(res % mod)