import heapq

x,y,a,b,c=map(int,input().split())
p=sorted(list(map(int,input().split())),reverse=True)
q=sorted(list(map(int,input().split())),reverse=True)
r=sorted(list(map(int,input().split())))

qu=[]

for i in range(x):
    heapq.heappush(qu,p[i])

for i in range(y):
    heapq.heappush(qu,q[i])

while r:
    rr=r.pop()

    if rr<qu[0]:
        break

    heapq.heappop(qu)
    heapq.heappush(qu,rr)

print(sum(qu))