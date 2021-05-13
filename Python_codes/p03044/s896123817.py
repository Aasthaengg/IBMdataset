from collections import deque
N = int(input())
connection =[[] for i in range(N)]
for i in range(1,N):
    u,v,w = (int(x) for x in input().split())
    u -=1
    v -=1
    connection[u].append((v,w))
    connection[v].append((u,w))
#
start=0
node =[None]*N
node[start] =0
dq =deque()
dq.append(start)

#
while dq:
    sarch =dq.popleft()
    for nv,w in connection[sarch]:
        if node[nv] is None:
            node[nv] = (node[sarch] +w) %2
            dq.append(nv)   
print(*node,sep="\n")