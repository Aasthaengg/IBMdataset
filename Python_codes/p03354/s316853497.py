import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(200000)
N,M=map(int,input().split())
p=tuple(map(lambda x: int(x)-1,input().split()))
l=[[] for i in range(N)]
for i in range(M):
    x,y=map(lambda x: int(x)-1,input().split())
    l[x].append(y)
    l[y].append(x)
g=[None]*N
c=0
def hu(n,c):
    for i in l[n]:
        if g[i]==None:
            g[i]=c
            hu(i,c)
for i in range(N):
    if g[i]==None:
        g[i]=c
        hu(i,c)
        c+=1
a=0
for i in range(N):
    if g[i]==g[p[i]]:
        a+=1
print(a)