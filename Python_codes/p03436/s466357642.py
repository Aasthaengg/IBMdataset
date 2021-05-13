import heapq

max_d = 10**9
dest_vecs = [(1,0), (0,1), (-1,0), (0, -1)]

def solve():
    H,W = map(int, input().split())
    
    S = [list(input()) for _ in range(H)]
    wall_num = sum(S_row.count('#') for S_row in S)
    
    # 最短経路を求める
    d = [[max_d]*W for _ in range(H)]
    d[0][0] = 0
    prev = [[None]*W for _ in range(H)]
    heap_queue = [(0,0,0)]
    while heap_queue:
        src_distance,y,x = heapq.heappop(heap_queue)
        for dy,dx in dest_vecs:
            ty = y+dy
            tx = x+dx
            if ty < 0 or ty >= H or tx < 0 or tx >= W or S[ty][tx] == '#':
                continue
            
            if d[ty][tx] > src_distance+1:
                d[ty][tx] = src_distance+1
                prev[ty][tx] = (y,x)
                heapq.heappush(heap_queue, (src_distance+1, ty, tx))
                
    ret = -1
    if d[H-1][W-1] < max_d:
        ret = H*W-d[H-1][W-1]-wall_num-1
    
    print(ret)
    
solve()