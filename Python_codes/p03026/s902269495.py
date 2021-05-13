from collections import deque

N = int(input())
lines = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    lines[a-1].append(b-1)
    lines[b-1].append(a-1)

c = list(map(int,input().split()))
c.sort(reverse=True)

not_visited = [-1]*N
not_visited[0] = 0
stack = deque()
stack.append(0)

ans = [0]*N
ans[0] = c[0]

cut = 1
while stack:
    now = stack.popleft()
    for nex in lines[now]:
        if not_visited[nex] == -1:
            ans[nex] = c[cut]
            not_visited[nex] =  not_visited[now] + 1
            cut += 1
            stack.append(nex)

print(sum(c[1:]))
print(*ans)