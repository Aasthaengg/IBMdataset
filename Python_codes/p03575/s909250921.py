n,m = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(m)]

from collections import defaultdict
from collections import deque
d=defaultdict(list)
for l in L:
    d[l[0]-1].append(l[1]-1)
    d[l[1]-1].append(l[0]-1)

#print(d)

# 辺を切断した状態で幅優先探索をしてすべての頂点に行けるか
def check_path(hen):
        
    visit=[False]*n
    q=deque([0])
    
#    print('L=',L)
#    print('hen=',hen)
    
    while q:
        node = q.popleft()
#        print('current->', node)
        visit[node]=True
        Nexts = d[node]
        for nxt in Nexts:
            if visit[nxt]:
#                print(nxt, ' is already visited.')
                continue
            
            if node+1 not in L[hen] or nxt+1 not in L[hen]:
#                print('next->', nxt)
                q.append(nxt)
    
#    print('visit=', visit)
    return all(visit)
    
cnt=0
for i in range(m):
    if not check_path(i):
        cnt+=1

print(cnt)