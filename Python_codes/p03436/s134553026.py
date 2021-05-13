import queue

h, w = map(int, input().split())
S = [input() for _ in range(h)]
n_black = 0
for s in S:
    n_black += s.count('#')

q = queue.Queue()
if S[0][0] == '.': 
    q.put((0, 0))
else: 
    print(-1)
    exit()

dist = [[-1] * w for _ in range(h)]
dist[0][0] = 1

while True:
    i, j = q.get()

    for ni, nj in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if S[ni][nj] == '.' and dist[ni][nj] == -1:
            q.put((ni, nj))
            dist[ni][nj] = dist[i][j] + 1
    
    if q.empty(): break

if dist[-1][-1] == -1: print(-1)
else: print(h * w - dist[-1][-1] - n_black)
