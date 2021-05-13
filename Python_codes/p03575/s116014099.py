import copy
from collections import deque
n,m = map(int,input().split())
a = [0 for _ in range(m)]
b = [0 for _ in range(m)]
joint = [[]for _ in range(n)]
for i in range(m):
    a[i],b[i] = map(int,input().split())
    a[i] -= 1
    b[i] -= 1
    joint[a[i]].append(b[i])
    joint[b[i]].append(a[i])

ans = 0
jointdef = copy.deepcopy(joint)
for i in range(m):
    joint = copy.deepcopy(jointdef)
    joint[a[i]].remove(b[i])
    joint[b[i]].remove(a[i])
    
    looked = [1 for _ in range(n)]
    looked[0] = 0
    queue = deque([0])
    while(queue):
        now = queue.popleft()
        for i in joint[now]:
            if looked[i]:
                queue.append(i)
                looked[i] = 0
    if sum(looked) != 0:
        ans += 1
print(ans)