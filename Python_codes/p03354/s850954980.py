N, M = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    P[i] -= 1
T = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x-=1
    y-=1
    T[x].append(y)
    T[y].append(x)

s1 = set()
def dfs(x):
    s1.add(x)
    s2 = set([x])
    stack = [x]
    while stack:
        u = stack.pop()
        for v in T[u]:
            if v not in s1 and v not in s2:
                s1.add(v)
                s2.add(v)
                stack.append(v)
    return s2

ans = 0
for i in range(N):
    if i in s1:
        continue
    I = dfs(i)
    PI = set(P[i] for i in I)
    ans += len(I.intersection(PI))
print(ans)