n, q = map(int, input().split())
tree = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(lambda x:int(x) - 1, input().split())
    tree[a].append(b)
    tree[b].append(a)

counter = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    counter[p-1] += x

visited = set()
stack = [0]
while stack:
    i = stack.pop()
    visited.add(i)
    for j in tree[i]:
        if not j in visited:
            counter[j] += counter[i]
            stack.append(j)
print(' '.join(map(str, counter)))