import sys
input=sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)
n=int(input())
edges=[[] for i in range(n)]
for i in range(n-1):
    a,s=map(int,input().split())
    a-=1;s-=1
    edges[a].append(s);edges[s].append(a)

def bfs(pre,now):
    for  i in edges[now]:
        if i==pre:continue
        if i==n-1:return[n-1,now]
        v=bfs(now,i)
        if v:v.append(now);return v
l=bfs(-1,0)
ll=len(l)
snuke_last=-(-ll//2)
table=[-1]*n
def c(now,pre):
    if table[now]!=-1:return table[now]
    if len(edges[now])>1:
        table[now]=1+sum(c(i,now) for i in edges[now] if i!=pre)
        return table[now]
    table[now]=1
    return 1
l=l[::-1]

d=c(l[snuke_last],l[snuke_last-1])

print("Fennec") if n-d>d else print("Snuke")
"""
1
2
3
4
567
"""