n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u-1].append((v-1, w))
    tree[v-1].append((u-1, w))

stack = [0]
color = [-1] * n
color[0] = 0
while stack:
    v = stack.pop()
    for child, w in tree[v]:
        if color[child] < 0:
            color[child] = (color[v] + w) % 2
            stack.append(child)
for i in color:
    print(i)