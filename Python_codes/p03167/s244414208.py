h,w = map(int, input().split())
l = [None]*h
for i in range(h):
    l[i] = list(input())
ans = [[0 for _ in range(w)] for _ in range(h)]
ans[0][0] = 1
mod = 7+10**9
for i in range(h):
    for j in range(w):
        if ans[i][j] == 0 or l[i][j] == "#":
            continue
        if i+1 < h:
            ans[i+1][j] += ans[i][j]
            ans[i+1][j] %= mod
        if j+1 < w:
            ans[i][j+1] += ans[i][j]
            ans[i][j+1] %= mod
print(ans[-1][-1])