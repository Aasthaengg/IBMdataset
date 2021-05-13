N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N-1)]
C = list(map(int,input().split()))
C.sort()
es = [[] for _ in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

stack = [0]
ans = [-1] * N
ans[0] = C.pop()
m = 0
while stack:
    v = stack.pop()
    for to in es[v]:
        if ans[to] >= 0: continue
        ans[to] = C.pop()
        m += ans[to]
        stack.append(to)
print(m)
print(*ans)