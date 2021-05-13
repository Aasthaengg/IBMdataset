ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
def gtr(n):
    tree = [[] for i in range(n)]
    for i in range(n-1):
        u,v =ma()
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    return tree
mod=10**9+7
n,k =ma()
tree = gtr(n)
stack = collections.deque()
stack.append(0)
visited=[True]+[False]*(n-1)
col = [k]*n
while stack:
    s = stack.pop()
    if s==0:
        cnt=k-1
    else:
        cnt=k-2
    for node in tree[s]:
        if not visited[node]:
            visited[node]=True
            stack.append(node)
            col[node]= max(0,cnt)
            cnt-=1
ans=1
for c in col:
    ans=ans*c%mod
print(ans)
