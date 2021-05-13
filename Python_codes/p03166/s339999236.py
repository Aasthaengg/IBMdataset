n,m=map(int,input().split())
edge=[[] for _ in range(n)]
arrive=[0]*n
ready=[]
for i in range(m):
    x,y=map(int,input().split())
    edge[x-1].append(y-1)
    arrive[y-1]+=1
for i in range(n):
    if arrive[i]==0:
        ready.append(i)

path_num=[0]*n
while ready:
    depart=ready.pop()
    for to in edge[depart]:
        path_num[to]=max(path_num[to],path_num[depart]+1)
        arrive[to]-=1
        if arrive[to]==0:
            ready.append(to)
print(max(path_num))