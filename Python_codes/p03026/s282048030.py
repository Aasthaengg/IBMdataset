from collections import deque
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)
C = list(map(int, input().split()))
C.sort(reverse=True)
q = deque([0])
visited = [False] * N
ans = {}
ans[0] = C[0]
visited[0] = True
pointa = 1
while len(q):
    v = q.pop()
    for e in tree[v]:
        if visited[e]:
            continue
        visited[e] = True
        ans[e] = C[pointa]
        pointa += 1
        q.append(e)
num = []
for i in range(N):
    num.append(str(ans[i]))
print(sum(C[1:]))
print(" ".join(num))
