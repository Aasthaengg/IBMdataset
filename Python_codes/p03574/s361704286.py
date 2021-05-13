h, w = map(int, input().split())

s = [input() for _ in range(h)]
ans = ['' for _ in range(h)]

for y in range(h):
    for x in range(w):
        if s[y][x] == '.':
            cnt = 0
            for dy in range(-1, 2, 1):
                for dx in range(-1, 2, 1):
                    if 0 <= x+dx < w and 0 <= y+dy < h:
                        if s[y+dy][x+dx] == '#':
                            cnt += 1
            ans[y] += str(cnt)
        else:
            ans[y] += '#'

for t in ans:
    print(t)