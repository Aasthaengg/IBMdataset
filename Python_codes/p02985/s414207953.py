N, K = map(int, input().split())
MOD = 10**9+7
edge = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(lambda x:int(x)-1, input().split()) # 0-indexed
    edge[a].append(b)
    edge[b].append(a)

def P(n, k):
    ans = 1
    for i in range(k):
        ans *= n
        ans %= MOD
        n -= 1
    return ans

visit = [False]*N

def dfs(v):
    Stack = [v]
    visit[v] = True
    ans = K
    while Stack:
        v = Stack.pop()
        if v == 0:
            color = K-1
            ans *= P(color, len(edge[v]))
            ans %= MOD
        else:
            color = K-2
            child = 0
            for i in edge[v]:
                if not visit[i]:
                    child += 1
            ans *= P(color, child)
            ans %= MOD
        for i in edge[v]:
            if not visit[i]:
                visit[i] = True
                Stack.append(i)
    return ans

print(dfs(0))


