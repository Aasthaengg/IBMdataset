import sys
sys.setrecursionlimit(10000000)

n,q=map(int,input().split())
lis=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    lis[a-1].append(b-1)
    lis[b-1].append(a-1)
p_list=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    p_list[p-1]+=x
close=set()
def dfs(n):
    close.add(n)
    for e in lis[n]:
        if e not in close:
            p_list[e]+=p_list[n]
            dfs(e)
dfs(0)
for p in p_list: print(p,end=" ")