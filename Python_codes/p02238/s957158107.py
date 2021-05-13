n = int(input())
G = [[] for _ in range(n)]
for _ in range(n):
    u, k, *v = map(int, input().split())
    u -= 1
    G[u].extend(v)
seen = [False] * n
d = [-1] * n
f = [-1] * n
t = 1

def dfs(v):
    global t
#     print(v+1, t)
    d[v] = t
    t += 1
    seen[v] = True
    for next_v in G[v]:
        next_v -= 1
        if not seen[next_v]:
            t = dfs(next_v)
    f[v] = t
    t += 1
    return t

def main():
#     todo = []
#     seen[0] = True
    for i in range(n):
        if not seen[i]:
            dfs(i)
    for i in range(n):
        print(i+1, d[i], f[i])
#     print(G)

if __name__ == "__main__":
    main()
