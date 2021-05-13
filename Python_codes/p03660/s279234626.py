import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N = I()

Graph = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = MI()
    Graph[a].append(b)
    Graph[b].append(a)

Fennec = [-1]*(N+1)  # Fennec の各頂点への最短距離
Snuke = [-1]*(N+1)  # Snuke の各頂点への距離

from collections import deque

q1 = deque([1])
q2 = deque([N])
Fennec[1] = 0
Snuke[N] = 0
while q1:
    n = q1.pop()
    for d in Graph[n]:
        if Fennec[d] == -1:
            Fennec[d] = Fennec[n] + 1
            q1.appendleft(d)
while q2:
    n = q2.pop()
    for d in Graph[n]:
        if Snuke[d] == -1:
            Snuke[d] = Snuke[n] + 1
            q2.appendleft(d)
            
a = sum(Fennec[i] <= Snuke[i] for i in range(1,N+1))
print('Fennec' if a >= N//2+1 else 'Snuke')
