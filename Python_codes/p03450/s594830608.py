import sys
sys.setrecursionlimit(10**7)

n,m=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(m):
    l,r,d=map(int,input().split())
    g[l-1].append([r-1,d])
    g[r-1].append([l-1,d*(-1)])
f=[False for _ in range(n)]

def dfs(s,x):
    f[s] = x
    for sg in g[s]:
        if type(f[sg[0]]) == bool:
            if not dfs(sg[0],sg[1]+x):
                return False
        else:
            if f[sg[0]] - f[s] != sg[1]:
                return False
    return True

def main():
    for i in range(n):
        if type(f[i]) == bool:
            if not dfs(i,1):
                return "No"
    return "Yes"

print(main())