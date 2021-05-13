h, w = map(int, input().split())
tizu = [input() for _ in range(h)]
check = [[False for _ in range(w)] for _ in range(h)]
ans = [[1 for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if check[i][j]:
            continue
        if tizu[i][j] == "#":
            continue
        pos = [i]
        cnt = 0
        for k in range(i + 1, h):
            if tizu[k][j] == "#":
                break
            pos.append(k)
            cnt += 1
        for k in range(i - 1, -1, -1):
            if tizu[k][j] == "#":
                break
            pos.append(k)
            cnt += 1
        for l in pos:
            ans[l][j] += cnt
            check[l][j] = True

check = [[False for _ in range(w)] for _ in range(h)]
max_ans = 0
for i in range(h):
    for j in range(w):
        if check[i][j]:
            continue
        if tizu[i][j] == "#":
            continue
        pos = [j]
        cnt = 0
        for k in range(j + 1, w):
            if tizu[i][k] == "#":
                break
            pos.append(k)
            cnt += 1
        for k in range(j - 1, -1, -1):
            if tizu[i][k] == "#":
                break
            pos.append(k)
            cnt += 1
        for l in pos:
            ans[i][l] += cnt
            check[i][l] = True
            max_ans = max(max_ans, ans[i][l])
print(max_ans)