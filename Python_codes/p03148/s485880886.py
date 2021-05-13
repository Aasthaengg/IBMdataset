import heapq
from sys import stdin

N,K = map(int,input().split())

sushi = {}

for i in range(N):
    t,d = map(int, stdin.readline().split())
    if t in sushi.keys():
        sushi[t].append(d)
    else:
        sushi[t] = [d]

P = []
Q = []

for x in sushi.keys():
    sushi[x].sort(reverse = True)
    P.append(sushi[x][0])
    
    for i in range(1,len(sushi[x])):
        Q.append(sushi[x][i])

heapq.heapify(P)

Q = list(map(lambda x:-x,Q))
heapq.heapify(Q)

while len(P) > K:
    m = heapq.heappop(P)
    heapq.heappush(Q,-m)

cur = 0

if K <= len(sushi.keys()):
    max_variation = K
else:
    max_variation = len(sushi.keys())
    for _ in range(K-max_variation):
        cur -= heapq.heappop(Q)

cur += sum(P)
ans = cur + max_variation**2

for i in range(max_variation-1):
    p = heapq.heappop(P)
    cur -= p
    q = -heapq.heappushpop(Q,-p)
    cur += q
    ans = max(ans,cur+(max_variation-i-1)**2)

print(ans)