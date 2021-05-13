import queue

H, W = map(int, input().split())
S = []

for _ in range(H):
    S.append(list(input()))

SS = []
for _ in range(H):
    SSS = []
    for __ in range(W):
        SSS.append(-1)
    SS.append(SSS)

SS[0][0] = 0

sp = (0, 0, 0)
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

q = queue.Queue()
q.put(sp)

ans = -1
complete = False
while not q.empty():

    n = q.get()
    if n[0] == W-1 and n[1] == H-1:
        ans = n[2]
        complete = True
        break

    for d in range(4):
        nx = n[0] + dx[d]
        ny = n[1] + dy[d]

        if W > nx >= 0 and H > ny >= 0 and SS[ny][nx] == -1 and S[ny][nx] != '#':
            q.put((nx, ny, n[2]+1))
            SS[ny][nx] = n[2] + 1

wcnt = 0
for _ in range(H):
    for __ in range(W):
        if S[_][__] == '.':
            wcnt += 1
if complete:
    print(wcnt - ans - 1)
else:
    print(-1)