from collections import deque

N = int(input())
tree = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].add(b - 1)
    tree[b - 1].add(a - 1)
C = sorted(list(map(int, input().split())))

ans = [0] * N

print(sum(C[:-1]))

ans[0] = C.pop()
n = min(tree[0])
ans[n] = C.pop()

d = deque([0, n])
visited = set(d)
while d:
    x = d.pop()
    for new_x in tree[x]:
        if new_x not in visited:
            ans[new_x] = C.pop()
            d.append(new_x)
            visited.add(new_x)

print(*ans)
