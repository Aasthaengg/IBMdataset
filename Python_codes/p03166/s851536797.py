from collections import deque

N,M = [int(v) for v in input().split()]
ad_list = [[] for _ in range (N+1)]
ad_num = [0 for _ in range(N)]
topo = []

for _ in range(M):
    l,r = [int(v) for v in input().split()]
    ad_list[l].append(r)
    ad_num[r-1] += 1

for i in range(1,N+1):
    if ad_num[i-1] == 0:
        topo.append([i,0])
queue = deque(topo[:])
while queue:
    n1,cnt = queue.popleft()
    for n2 in ad_list[n1]:
        ad_num[n2-1] -= 1
        if ad_num[n2-1] == 0:
            topo.append([n2,cnt+1])
            queue.append([n2,cnt+1])
print(max([v[1] for v in topo]))
