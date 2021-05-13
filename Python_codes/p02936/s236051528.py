import sys
input=sys.stdin.buffer.readline
inputs=sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)
n, q = map(int, input().split())
edges=[[] for i in range(1+n)]
for i in range(n-1):
    """#weighted->erase_,__,___=map(int,input().split())
    edges[_].append((__,___))
    edges[__].append((_,___))
    """
    _,__=map(int,input().split())
    edges[_].append(__)
    edges[__].append(_)
    """
"""#weighted->erase
cnt=[0]*(1+n)
for i in range(q):
    x,p=map(int,input().split())
    cnt[x]+=p
def f(now,pars_value,par):
    cnt[now]+=pars_value
    a=cnt[now]
    for i in edges[now]:
        if i!=par:f(i,a,now)
f(1,0,-1)
print(*cnt[1:])