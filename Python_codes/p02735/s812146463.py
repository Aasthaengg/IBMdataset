from collections import deque

def solve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    INF = 10 ** 9
    d = [[INF] * W for i in range(H)]
    d[0][0] = 1 if A[0][0] == '#' else 0

    prepare = 1 if A[0][0] == '#' else 0
    q = deque([(prepare, 0, 0)])
    while q:
        c, x, y = q.popleft()
        for a, b in [(1,0), (0,1)]:
            nx, ny = x+a, y+b
            if nx >= W or ny >= H: continue
            k = 1 if A[y][x] != A[ny][nx] else 0
            if c+k >= d[ny][nx]: continue
            d[ny][nx] = c+k
            q.append((c+k, nx, ny))

    return (d[H-1][W-1]+1)//2

print(solve())