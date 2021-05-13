h, w = map(int, input().split())
s = [[]for _ in range(h)]
for i in range(h):
    s[i] = list(input())

ans = [["." for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if i != 0:
                if s[i-1][j] == "#":
                    ans[i-1][j] = "#"
            if i != h-1:
                if s[i+1][j] == "#":
                    ans[i+1][j] = "#"
            if j != 0:
                if s[i][j-1] == "#":
                    ans[i][j-1] = "#"
            if j != w-1:
                if s[i][j+1] == "#":
                    ans[i][j+1] = "#"
print("Yes" if s == ans else "No")
