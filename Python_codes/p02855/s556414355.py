H, W, K = map(int, input().split())
s = []
for _ in range(H):
    s.append(list(input()))
cnt = 1
for y in range(H):
    for x in range(W):
        if s[y][x] == '#':
            s[y][x] = cnt
            cnt += 1

for y in range(H):
    for x in range(1, W):
        if s[y][x] == '.':
            s[y][x] = s[y][x - 1]
    for x in range(W - 2, -1, -1):
        if s[y][x] == '.':
            s[y][x] = s[y][x + 1]
for x in range(W):
    for y in range(1, H):
        if s[y][x] == '.':
            s[y][x] = s[y - 1][x]
    for y in range(H - 2, -1, -1):
        if s[y][x] == '.':
            s[y][x] = s[y + 1][x]
# print(s)
for y in range(H):
    for x in range(W):
        if x != W - 1:
            print(s[y][x], end=' ')
        else:
            print(s[y][x], end='\n')
