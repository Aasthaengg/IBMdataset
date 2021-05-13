import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
l=[list(map(int,input().split())) for _ in range(n-1)]

nbr=[[] for _ in range(n)]
for i in range(n-1):
    nbr[l[i][0]-1].append(l[i][1]-1)
    nbr[l[i][1]-1].append(l[i][0]-1)
def sm(i,p):
    s=0
    for x in nbr[i]:
        if x!=p:s+=sm(x,i)
    return s+1
flg=False
f=0
c=[]
def dfs(i,p):
    global flg
    global c
    if i==n-1:flg=True
    if not flg:
        for x in nbr[i]:
            if x!=p:dfs(x,i)
            if flg:break
    if flg:
        c.append(i)
dfs(0,-1)
idx=(len(c)+1)//2
print('Fennec' if sm(c[::-1][idx],c[::-1][idx-1])*2<n else 'Snuke')