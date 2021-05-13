import sys
sys.setrecursionlimit(1000000)


n,m=map(int,input().split())

p=[[] for _ in range(n)]

for _ in range(m):
    x,y=map(int,input().split())
    p[x-1].append(y-1)

f=[-1 for _ in range(n)]

def calc(x):
    if f[x]!=-1:
        return f[x]
    if len(p[x])==0:
        f[x]=0
        return 0
    f[x]=max([calc(i) for i in p[x]])+1
    return f[x]

m=0
for i in range(n):
    if f[i]!=-1:
        continue
    m=max(m,calc(i))
print(m)
