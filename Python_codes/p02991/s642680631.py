import heapq as h

N,M=map(int,input().split())
hen={(i,j):[] for i in range(0,N) for j in range(0,3)}
for i in range(0,M):
    u,v=map(int,input().split())
    hen[(u-1,0)].append((v-1,1))
    hen[(u-1,1)].append((v-1,2))
    hen[(u-1,2)].append((v-1,0))

S,T=map(int,input().split())

start=(S-1,0)
goal=(T-1,0)

distance={(i,j):-1 for i in range(0,N) for j in range(0,3)}

q=[]
q.append(start)
distance[start]=0
h.heapify(q)
sub=[]
h.heapify(sub)
while q!=[]:
    while q!=[]:
        x=h.heappop(q)
        for p in hen[x]:
            if distance[p]==-1:
                h.heappush(sub,p)
                distance[p]=distance[x]+1
        #何らかの操作
        #ここでsubキューに次に使うものを格納
        if q==[]:
            q=sub
            sub=[]
            h.heapify(sub)
            break

if distance[goal]==-1:
    print(-1)
else:
    print(distance[goal]//3)