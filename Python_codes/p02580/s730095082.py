import bisect

H, W, M = map(int,input().split())
hw = [list(map(int,input().split())) for _ in range(M)]
hw.sort()

rows, columns = [0]*H, [0]*W
for h, w in hw:
    rows[h-1] += 1
    columns[w-1] += 1
max_r, max_c = max(rows), max(columns)

argmax_r, argmax_c = [], []
for i in range(H):
    if max_r == rows[i]:
        argmax_r.append(i)

for i in range(W):
    if max_c == columns[i]:
        argmax_c.append(i)

for r in argmax_r:
    for c in argmax_c:
        idx = bisect.bisect_left(hw, [r+1, c+1])
        if idx == M or hw[idx] != [r+1,c+1]:
            print(max_r + max_c)
            exit()

print(max_r + max_c - 1)