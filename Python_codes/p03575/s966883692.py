import sys

sys.setrecursionlimit(10**7)


def dfs(x):
    if arrival[x-1]==1:
        return
    else:
        arrival[x-1]=1
        for i in mapi[x-1]:
            dfs(i)
        return

n,m=map(int,input().split())

l=[]
for i in range(m):
    l.append(list(map(int,input().split())))

count=0
for i in range(m):
    li=l[0:i]+l[i+1:m]
    mapi=[[] for a in range(n)]
    for j in range(m-1):
        mapi[li[j][0]-1].append(li[j][1])
        mapi[li[j][1]-1].append(li[j][0])
    arrival=[0 for a in range(n)]
    dfs(1)
    if 0 in arrival:
        count+=1
print(count)