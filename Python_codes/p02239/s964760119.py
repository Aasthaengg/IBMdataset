n=int(input())
dic=[[] for i in range(n)]
for i in range(n):
    a=list(map(int,input().split()))
    a=a[2:]
    dic[i]=list(map(lambda x:x-1,a))

from collections import deque
d=deque()
d.append(0) #始点
completed=[False]*n
distance=[999]*n
distance[0]=0
while d:
    now=d.popleft()
    completed[now]=True
    for x in dic[now]: #次の頂点探し
        if completed[x]==False: #その頂点に進んでもよいか
            distance[x]=min(distance[now]+1,distance[x])  #処理
            d.append(x)
for i in range(n):
    if distance[i]==999:
        distance[i]=-1
    print(i+1,distance[i])
    
