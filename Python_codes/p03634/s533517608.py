from collections import defaultdict
from collections import deque
n = int(input())
tree = defaultdict(list)
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

def distance(k):
    seen = set()
    dis_l = {}
    d = 0
    stack = deque([[tree[k], d]])
    flag = True
    while stack:
        connect, d = stack.popleft()
        for i in connect:
            if i[0] not in seen:
                seen.add(i[0])
                d += i[1]
                dis_l[i[0]] = d
                stack.append([tree[i[0]], d])
                d -= i[1]
    return dis_l

q, k = map(int, input().split())
dis_l = distance(k)
for i in range(q):
    x, y = map(int, input().split())
    print(dis_l[x] + dis_l[y])