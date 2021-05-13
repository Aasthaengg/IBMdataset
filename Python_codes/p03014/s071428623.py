h, w = list(map(int, input().split()))
s = []
up, down, right, left = [
    [[0 for _ in range(w)] for _ in range(h)] for _ in range(4)]
for _ in range(h):
    s.append(list(input()))

for j in range(w):
    for i in range(h - 1, -1, -1):
        if s[i][j] == ".":
            if i == h - 1:
                down[i][j] = 1
            else:
                down[i][j] = down[i + 1][j] + 1

for j in range(w):
    for i in range(h):
        if s[i][j] == ".":
            if i == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i - 1][j] + 1

for i in range(h):
    for j in range(w - 1, -1, -1):
        if s[i][j] == ".":
            if j == w - 1:
                right[i][j] = 1
            else:
                right[i][j] = right[i][j + 1] + 1

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j - 1] + 1

res = 0
for i in range(h):
    for j in range(w):
        lit = up[i][j] + down[i][j] + right[i][j] + left[i][j] - 3
        res = max(res, lit)
print(res)
