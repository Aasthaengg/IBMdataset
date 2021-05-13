dic = {1:0,0:1}

from collections import deque 
#スタック
q = deque([])#append pop

N = int(input())
#木
tree = [[]for i in range(0,N+1,1)]
for i in range(1,N,1):
    u,v,w = map(int,input().split())
    tree[u].append([v,w])
    tree[v].append([u,w])
ans = [0]*(N+1)

q.append([1,0,0])#今回のノード、距離、前回のノード

while len(q)>0:
    now,dist,pre = q.pop()
    ans[now] = (ans[pre] + dist%2)%2
    for i in tree[now]:
        if i[0]!=pre:
            q.append([i[0],i[1],now])

for i in range(1,N+1,1):
    print(ans[i])