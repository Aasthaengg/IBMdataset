N = int(input())
pos = []
for _ in range(N):
    x,y = [int(v) for v in input().split()]
    pos.append((x,y))

path = []
def dfs(state):
    if len(state) == N:
        path.append(state)
        return
    for i in range(N):
        if i not in state:
            nstate = state[:]
            nstate.append(i)
            dfs(nstate)

dfs([])
ans = 0
for p in path:
    n = p[0]
    tmp = 0
    for nn in p[1:]:
        tmp += (abs(pos[n][0] - pos[nn][0]) ** 2 + abs(pos[n][1] - pos[nn][1]) ** 2) ** (1/2)
    ans += (tmp / len(path))
print(ans)
