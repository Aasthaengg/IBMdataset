N,M=list(map(int,input().split()))

ad={} #近接リスト
for n in range(N):
    ad[n+1]=set([])
    
depth={} #深さ
for n in range(N):
    depth[n+1]=0
    
parent={}
for n in range(N):
    parent[n+1]=0
    
visit_dict={} #発見しているか保持（-1:未発見、0:発見、1:訪問済）
for n in range(N):
    visit_dict[n+1]=-1
    
for m in range(M):
    a,b=list(map(int,input().split()))
    ad[a].add(b)
    ad[b].add(a)

# 幅優先探索
from collections import deque

que = deque([1])
visit = deque([])
depth[1]=1
visit_dict[1]=0

i=0
while len(que) > 0:
    i+=1
    start=que[0]
    for _ in ad[start]:
        if visit_dict[_] != -1:
            continue
        else:
            depth[_]=depth[start]+1
            parent[_]=start
            visit_dict[_]=0
            que.append(_)  
            
    visit_dict[start]=1
    visit.appendleft(que.popleft())
            

print('Yes')
for p in list(parent.keys())[1:]:
    print(parent[p])