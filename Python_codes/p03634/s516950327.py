from collections import deque

n = int(input())
ab = [[]for i in range(10**5)]
v=[0]*(10**5)
d=[float('INF')]*(10**5)
for i in range(n-1):
    a , b , c = map(int, input().split())
    ab[a-1].append((b-1,c))
    ab[b-1].append((a-1,c))
q , k = map(int, input().split())

k-=1
de=deque()
de.append((k,0))

d[k]=0
while de:
    now , dis = de.popleft()
    if dis > d[now]:
        continue

    for next , cost in ab[now]:
        if dis + cost < d[next]:
            d[next]= dis + cost
            de.append((next,dis+cost))

for i in range(q):
    x , y = map(int, input().split())
    x-=1
    y-=1
    print(d[x]+d[y])
