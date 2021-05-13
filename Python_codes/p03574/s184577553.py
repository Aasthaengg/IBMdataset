h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = [[""]*w for _ in range(h)]

if h == 1 and w == 1:
    if s[0][0] == "#":
        print("#")
    else:
        print(0)

elif h == 1:
    for j in range(w):
        if s[0][j] == ".":
            ans[0][j] = s[0][max(0, j - 1):min(w + 1, j + 2)].count("#")
        else:
            ans[0][j] = "#"

elif w == 1:
    for i in range(h):
        if i == 0:
            if s[i][0] == ".":
                ans[i][0] = s[i + 1][0].count("#")
            else:
                ans[i][0] = "#"
        elif i == h - 1:
            if s[i][0] == ".":
                ans[i][0] = s[i - 1][0].count("#")
            else:
                ans[i][0] = "#"
        else:
            if s[i][0] == ".":
                ans[i][0] = s[i - 1][0].count("#") + s[i+1][0].count("#")
            else:
                ans[i][0] = "#"

else:
    for i in range(h):
        for j in range(w):
            if i == 0:
                if s[i][j] == ".":
                    ans[i][j] = s[i][max(0, j - 1):min(w + 1, j + 2)].count("#") + s[i + 1][
                                                                                   max(0, j - 1):min(w + 1, j + 2)].count(
                        "#")
                else:
                    ans[i][j] = "#"
            elif i == h-1:
                if s[i][j] == ".":
                    ans[i][j] = s[i - 1][max(0, j - 1):min(w + 1, j + 2)].count("#") + s[i][max(0, j - 1):min(w + 1,
                                                                                                              j + 2)].count(
                        "#")
                else:
                    ans[i][j] = "#"
            else:
                if s[i][j] == ".":
                    ans[i][j] = s[i - 1][max(0, j - 1):min(w + 1, j + 2)].count("#") + s[i][max(0, j - 1):min(w + 1,
                                                                                                              j + 2)].count(
                        "#") + s[i + 1][max(0, j - 1):min(w + 1, j + 2)].count("#")
                else:
                    ans[i][j] = "#"

[print(*k,sep="") for k in ans]