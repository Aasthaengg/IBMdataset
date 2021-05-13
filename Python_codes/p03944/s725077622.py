w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for i in range(n)]
l = [["." for i in range(w)] for j in range(h)]
for i in range(n):
    if xya[i][2] == 1:
        l = [["#" if j < xya[i][0] else "#" if l[k][j] == "#" else "." for j in range(w)] for k in range(h)]
    elif xya[i][2] == 2:
        l = [["#" if j >= xya[i][0] else "#" if l[k][j] == "#" else "." for j in range(w)] for k in range(h)]
    elif xya[i][2] == 3:
        l = [["#" if k < xya[i][1] else "#" if l[k][j] == "#" else "." for j in range(w)] for k in range(h)]
    elif xya[i][2] == 4:
        l = [["#" if k >= xya[i][1] else "#" if l[k][j] == "#" else "." for j in range(w)] for k in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if l[i][j] == ".":
            ans += 1
print(ans)