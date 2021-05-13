from collections import deque
N=int(input())
color=["white"]*(N+1)
rinsetu=[[] for i in range(N+1)]
for i in range(N):
    a,*b=list(map(int,input().split()))
    for idx,j in enumerate(b):
        if idx==0:continue
        rinsetu[a].append(j)
distance=[10**5]*(N+1)
distance[1]=0
def bfs():
    d = deque()
    d.append(1)
    while(d):
        num=d.popleft()
        color[num] = "black"
        for i in rinsetu[num]:
            if color[i]=="white":
                d.append(i)
                distance[i]=min(distance[num]+1,distance[i])

bfs()
for i in range(1,N+1):
    if distance[i]==10**5:distance[i]=-1
    print(i,distance[i])
