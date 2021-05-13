H, W, D = map(int, input().split())
# 1, 2, ..., H*Wの座標を記録
G = [(-10**9, -10**9) for _ in range(H * W + 1)]

for i in range(H):
    line = list(map(int, input().split()))
    for j in range(W):
        grid = int(line[j])
        G[grid] = (i, j)

# 1,2,...,H*Wまで行くために必要なコスト
cost = [0 for _ in range(H * W + 1)]
for i in range(D + 1, H * W + 1):
    cost_x = abs(G[i][0] - G[i - D][0])
    cost_y = abs(G[i][1] - G[i - D][1])
    cost[i] = cost[i - D] + cost_x + cost_y

ans = []

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    tmp = cost[r] - cost[l]
    ans.append(tmp)

# print(G)
# print(cost)

for i in ans:
    print(i)
