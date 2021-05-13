import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,M = MI()
G = {}
for i in range(1,N+1):
    G[(i,0)] = []
    G[(i,1)] = []
    G[(i,2)] = []
for _ in range(M):
    u,v = MI()
    G[(u,0)].append((v,1))
    G[(u,1)].append((v,2))
    G[(u,2)].append((v,0))

S,T = MI()

flag = [[-1]*3 for i in range(N+1)]

from collections import deque

q = deque([(S,0,0)])  # 頂点、mod 3、Sからの最短距離
while q:
    n,m,r = q.pop()
    for d,e in G[(n,m)]:
        if flag[d][e] != -1:
            continue
        else:
            flag[d][e] = r+1
            q.appendleft((d,e,r+1))

print(flag[T][0]//3)
