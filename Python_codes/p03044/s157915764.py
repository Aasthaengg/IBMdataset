
from collections import deque

n = int(input())
arr = [[] for _ in range(n) ]

for i in range(n-1):
    u,v,w =map(int,input().split())
    arr[u-1].append([v-1,w])
    arr[v-1].append([u-1,w])


queue = deque([0])
ans = [0]*n
checked = [0]*n

while queue:
    x =queue.popleft()
    checked[x] = -1
    dis = ans[x]
    for tup in arr[x]:
        if checked[tup[0]]> -1:
            ans[tup[0]]=(dis+tup[1])%2
            queue.append(tup[0])
print(*ans,sep='\n')
