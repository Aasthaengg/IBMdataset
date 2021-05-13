n, q = map(int, input().split())
tree_candidate = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree_candidate[a].append(b)
    tree_candidate[b].append(a)

tree = [[] for _ in range(n)]

app = set([0])

import queue
next = queue.Queue()
next.put(0)
# print(tree_candidate)
while not next.empty():
    i = next.get()
    for j in tree_candidate[i]:
        if not j in app:
            tree[i].append(j)
            app.add(j)
            next.put(j)

cnts = [0 for _ in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    cnts[p-1] += x
    # print(x, p, tree[p-1], cnts)

next = queue.Queue()
next.put(0)

while not next.empty():
    i = next.get()
    for j in tree[i]:
        cnts[j] += cnts[i]
        next.put(j)

for i in cnts:
    print(i, end=' ')