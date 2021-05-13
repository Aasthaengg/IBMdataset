from collections import deque
 
def solve(h, w, a):
    used = [[True] * (w+2) for _ in range(h+2)]
    que = deque()
    for r in range(h):
        used[r+1][1:-1] = map(lambda _:_=="#", a[r])
        for c in range(w):
            if a[r][c] == "#":
                que.append((r+1, c+1, 0))
    neighbors = [(1,0), (0,1), (-1,0), (0,-1)]
    while que:
        r, c, k = que.popleft()
        for dr, dc in neighbors:
            nr, nc = r+dr, c+dc
            if not used[nr][nc]:
                que.append((nr, nc, k+1))
                used[nr][nc] = True
    return k
 
h, w = map(int, input().split())
a = [input() for _ in range(h)]
print(solve(h, w, a))