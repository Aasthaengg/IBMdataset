ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
n,m = ma()

INF=10**15
x = [INF]*n
tree = [[] for i in range(n)]

for i in range(m):
    l,r,d=ma()
    tree[l-1].append((r-1,d))
    tree[r-1].append((l-1,-d))
f=True
def dfs(s):
    stack = collections.deque()
    stack.append((s,0))
    x[s]=0
    ret=True
    while stack:
        pre,c = stack.pop()
        for nex,d in tree[pre]:
            if x[nex]==INF:
                x[nex]=c+d
                stack.append((nex,c+d))
            else:
                if x[nex] !=c+d:
                    # print("pre,nex",pre,nex,x,c,d)
                    ret=False
    return ret
f=True
for i in range(n):
    if x[i]==INF:
        f&=dfs(i)
# print(x)
yn(f)
