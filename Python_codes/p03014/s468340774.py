h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

right = [[0]*w for _ in range(h)]
left = [[0]*w for _ in range(h)]
up = [[0]*w for _ in range(h)]
down = [[0]*w for _ in range(h)]

for i in range(h):
    if s[i][0] == ".":
        left[i][0] = 1
    if s[i][w-1] == ".":
        right[i][w-1] = 1

for j in range(w):
    if s[0][j] == ".":
        down[0][j] = 1
    if s[h-1][j] == ".":
        up[h-1][j] = 1
        
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if j > 0:
                left[i][j] = left[i][j-1] + 1
            if i > 0:
                down[i][j] = down[i-1][j] + 1

for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if s[i][j] == ".":
            if i < h-1:
                up[i][j] = up[i+1][j] + 1
            if j < w-1:
                right[i][j] = right[i][j+1] + 1
ans = 0
for i in range(h):
    for j in range(w):
        count = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3
        if ans < count:
            ans = count
print(ans)