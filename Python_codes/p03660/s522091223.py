# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(10**6)

def killme(num,lis):
    visited[num]=1
    if num==N-1:
        lis.append(num)
        for index,item in enumerate(lis):
            highway[item]=index
    else:
        for next_n in way[num]:
            if visited[next_n]==0:
                lis.append(num)
                killme(next_n,lis)
                lis.pop(-1)
    return 

def dfs(num,root):
    visited[num]=1
    cluster[root].append(num)
    for next_n in way[num]:
        if visited[next_n]==0 and highway[next_n]==-1:
            #print(next_n,root)
            dfs(next_n,root)
    return 

N=int(input())

way=[[] for i in range(N)]
visited=[0]*N
highway=[-1]*N

for _ in range(N-1):
    a,b=map(int,input().split())
    way[a-1].append(b-1)
    way[b-1].append(a-1)

killme(0,[])

#print(way)
#print(visited)
#print(highway)

visited=[0]*N
cluster=[[] for i in range(highway[-1]+1)]

for index,item in enumerate(highway):
    if item!=-1:
        dfs(index,item)

F=0
S=0
for i in range(highway[-1]+1):
    if i<=highway[-1]//2:
        F+=len(cluster[i])
    else:
        S+=len(cluster[i])

if F>S:
    print("Fennec")
else:
    print("Snuke")
#print(F,S)
    

