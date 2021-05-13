import sys
input = sys.stdin.readline
X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

AB = []
AC = []
BC = []
for a in A:
    for b in B:
        AB.append(a+b)
    for c in C:
        AC.append(a+c)
for b in B:
    for c in C:
        BC.append(b+c)
AB.sort(reverse=True)
AC.sort(reverse=True)
BC.sort(reverse=True)

import heapq
hq = []
for x in AB[:K]:
    for c in C:
        heapq.heappush(hq, -x-c)
for x in BC[:K]:
    for a in A:
        heapq.heappush(hq, -x-a)
for x in AC[:K]:
    for b in B:
        heapq.heappush(hq, -x-b)

ans = []
for _ in range(K):
    ans.append(-heapq.heappop(hq))
    heapq.heappop(hq)
    heapq.heappop(hq)
print(*ans, sep='\n')