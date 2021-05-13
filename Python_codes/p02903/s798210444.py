h, w, a, b = map(int, input().split())
ans = []
for _ in range(h):
    ans.append([0 for __ in range(w)])
for i in range(b):
    for j in range(w):
        ans[i][j] = (ans[i][j]+1)%2
for i in range(a):
    for j in range(h):
        ans[j][i] = (ans[j][i]+1)%2
for i in range(h):
    for j in range(w):
        if j != w-1:
            print(ans[i][j], end="")
        else:
            print(ans[i][j])