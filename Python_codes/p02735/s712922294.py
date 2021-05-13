import queue
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = float('inf')
q = queue.Queue()
vals = [[float('inf')]*w for _ in range(h)]
vals[0][0] = 0
q.put([0, 0])

while not q.empty():
    a = q.get()
    for i, j in ((1, 0), (0, 1)):
        x, y = a[0]+i, a[1]+j
        if 0 <= x < h and 0 <= y < w:
            if s[x][y] == '#' and s[a[0]][a[1]] == '.':
                if vals[x][y] > vals[a[0]][a[1]]+1:
                    vals[x][y] = vals[a[0]][a[1]]+1
                    q.put([x, y])
            elif vals[x][y] > vals[a[0]][a[1]]:
                vals[x][y] = vals[a[0]][a[1]]
                q.put([x, y])
ans = vals[-1][-1]
if s[0][0] == '#':
    ans += 1

print(ans)
