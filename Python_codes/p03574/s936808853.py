h, w = map(int, input().split())
ans = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    S = input()
    for j, s in enumerate(S):
        if s == "#":
            ans[i][j] = "#"
            if i != 0:
                if ans[i - 1][j] != "#":
                    ans[i - 1][j] += 1
            if j != 0:
                if ans[i][j - 1] != "#":
                    ans[i][j - 1] += 1
            if i != 0 and j != 0:
                if ans[i - 1][j - 1] != "#":
                    ans[i - 1][j - 1] += 1
            if j != w - 1:
                if ans[i][j + 1] != "#":
                    ans[i][j + 1] += 1
            if j != w - 1 and i != 0:
                if ans[i - 1][j + 1] != "#":
                    ans[i - 1][j + 1] += 1
            if i != h - 1:
                if ans[i + 1][j] != "#":
                    ans[i + 1][j] += 1
            if i != h - 1 and j != w - 1:
                if ans[i + 1][j + 1] != "#":
                    ans[i + 1][j + 1] += 1
            if i != h - 1 and j != 0:
                if ans[i + 1][j - 1] != "#":
                    ans[i + 1][j - 1] += 1

for a in ans:
    print("".join(map(str, a)))
