h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    done = [False] * w
    for j in range(w):
        if s[i][j] == "#":
            continue
        if done[j]:
            continue
        l = 0
        while j+l < w:
            if s[i][j+l] == "#":
                break
            l += 1
        for k in range(j, j+l):
            ans[i][k] += l
            done[k] = True
for j in range(w):
    done = [False] * h
    for i in range(h):
        if s[i][j] == "#":
            continue
        if done[i]:
            continue
        l = 0
        while i+l < h:
            if s[i+l][j] == "#":
                break
            l += 1
        for k in range(i, i+l):
            ans[k][j] += l
            done[k] = True
res = 0
for i in range(h):
    res = max(max(ans[i]), res)
res -= 1
print(res)