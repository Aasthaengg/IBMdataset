N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]
cur = [0] * N
edge = [0] * N
for i in range(N):
    edge[i] = G[i][0] - 1

day = 0
player = set(range(N))
cnt = 0
while len(player) > 0:
    day += 1
    game = set()
    for i in player:
        e = edge[i]
        if i == edge[e] and i != e:
            game.add(i)
            game.add(e)
    player = set()
    for j in game:
        cur[j] += 1
        c = cur[j]
        if c >= N - 1:
            edge[j] = j
        else:
            edge[j] = G[j][c] - 1
            player.add(j)

if min(cur) != N - 1:
    ans = -1
else:
    ans = day
print(ans)
