from collections import deque


H,W = map(int, input().split())

S = [input() for _ in range(H)]


"""
移動先の色が同じであれば、その部分は一回の操作でひっくり返せるので、黒から黒へ連続で移動していても操作回数は一回でOK

"""
INF = float("inf")
costs = [[INF for _ in range(W)] for _ in range(H)]

costs[0][0] = 0 if S[0][0] == "." else 1

q = deque()
q.append((costs[0][0], 0, 0))

while q:
    curr_cost, y, x = q.popleft()
    for dy, dx in [(1,0), (0,1)]:
        if y + dy >= H or x + dx >= W:
            continue
        nxt_cost = curr_cost if S[y][x] == S[y+dy][x+dx] else curr_cost + 1
        if nxt_cost < costs[y+dy][x+dx]:
            costs[y+dy][x+dx] = nxt_cost
            q.append((nxt_cost, y+dy, x+dx))


print((costs[-1][-1] + 1) // 2)
