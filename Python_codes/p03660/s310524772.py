N=int(input())
E=[[] for i in range(N)]

for i in range(N-1):
    x,y=map(int,input().split())
    x-=1
    y-=1
    E[x].append(y)
    E[y].append(x)


from collections import deque
BACK=[-1]*N

Q=deque([0])

while Q:
    x=Q.pop()

    for to in E[x]:
        if BACK[to]==-1:
            BACK[to]=x
            Q.append(to)

ROAD=[N-1]

while ROAD[-1]!=0:
    ROAD.append(BACK[ROAD[-1]])

LEN=len(ROAD)

COLOR=[-1]*N
QW=deque()
QB=deque()

for i in range(LEN//2):
    COLOR[ROAD[i]]=1
    QB.append(ROAD[i])

for i in range(LEN//2,LEN):
    COLOR[ROAD[i]]=0
    QW.append(ROAD[i])

SW=0
if LEN%2==1:
    SW+=1
SB=0

while QW:
    x=QW.pop()

    for to in E[x]:
        if COLOR[to]==-1:
            COLOR[to]=0
            SW+=1
            QW.append(to)

while QB:
    x=QB.pop()

    for to in E[x]:
        if COLOR[to]==-1:
            COLOR[to]=1
            SB+=1
            QB.append(to)

if SW>SB:
    print("Fennec")
else:
    print("Snuke")
