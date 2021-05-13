from heapq import heapify, heappush, heappop 

INF = 1001001001

N, Q = map(int, input().split())
STXs = [tuple(map(int, input().split())) for _ in range(N)]
Ds = [int(input()) for _ in range(Q)]

#S-X, T-X, X
future_block = [(S - X, T - X, X) for S, T, X in STXs]
future_block.append((INF, INF, INF)) #sentinel
heapify(future_block)

#T-X, X
current_block = [(INF, INF)] #sentinel
current_min_pair = (INF, INF)

for D in Ds:
    while future_block[0][0] <= D:
        s_x, t_x, x = heappop(future_block)
        if current_min_pair[1] > x:
            current_min_pair = (t_x, x)
        heappush(current_block, (t_x, x))
    
    search_min_flg = False
    while current_block[0][0] <= D:
        if current_min_pair == heappop(current_block):
            search_min_flg = True
    if search_min_flg:
        current_min_pair = min(current_block, key = lambda t: t[1])

    print(-1 if current_min_pair[1] == INF else current_min_pair[1])
