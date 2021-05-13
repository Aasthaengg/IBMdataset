h,w,k = map(int, input().split())
grid = []
cake = []
for i in range(h):
    s = input()
    grid.append(s)
    cake.append(s.count('#'))
num = 0

ans = [[0 for j in range(w)] for i in range(h)]
first = []

for i in range(h):
    if cake[i] == 0 and first == []:
        continue
    if cake[i]:
        num += 1
        cnt = 0
        for j in range(w):
            ans[i][j] = num
            if grid[i][j] == '#':
                cnt += 1
                if cnt < cake[i]:
                    num += 1
        if first == []:
            for j in range(w):
                first.append(ans[i][j])
    else:
        for j in range(w):
            ans[i][j] = ans[i-1][j]

for i in range(h):
    if ans[i][0] != 0:
        continue
    for j in range(w):
        ans[i][j] = first[j]
[print(*i) for i in ans]
