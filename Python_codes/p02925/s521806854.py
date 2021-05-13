import sys
input = sys.stdin.readline
from collections import *

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
serial = [[0]*N for _ in range(N)]
c = 0

for i in range(N):
    for j in range(i+1, N):
        serial[i][j] = c
        serial[j][i] = c
        c += 1
        
ins = [0]*(N*(N-1)//2)
outs = defaultdict(list)

for i in range(N):
    for j in range(1, N-1):
        s = serial[i][A[i][j-1]-1]
        t = serial[i][A[i][j]-1]
        ins[t] += 1
        outs[s].append(t)

q = deque([i for i in range(N*(N-1)//2) if ins[i]==0])
ans = 0

while True:
    if len(q)==0:
        break
    
    nq = deque([])
    
    while q:
        v = q.popleft()
        
        for nv in outs[v]:
            ins[nv] -= 1
            
            if ins[nv]==0:
                nq.append(nv)
    
    ans += 1
    q = nq

if ins!=[0]*(N*(N-1)//2):
    print(-1)
    exit()
    
print(ans)