N = int(input())
tree = [[] for _ in range(N)]

for i in range(N-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append((b, c))
    tree[b].append((a, c))

Q, K = map(int, input().split())
K -= 1

depth = [0 for _ in range(N)]

def dfs(v, p = -1, d = 0):
    St = []
    St.append([v, p, d])
    # 空のシーケンスは偽になる
    while St:
        cur = St.pop()
        depth[cur[0]] = cur[2]
        for i, j in tree[cur[0]]:
            if i == cur[1]:
                continue
            St.append([i, cur[0], cur[2] + j])

dfs(K)

for i in range(Q):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    print (depth[x] + depth[y])
