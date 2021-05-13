h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
s = [["."] * (w+2)] + [[".", *i, "."] for i in s] + [["."] * (w+2)]
ans = "Yes"
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == "#":
            if s[i-1][j] == "." and s[i][j-1] == "." and s[i][j+1] == "." and s[i+1][j] == ".":
                ans = "No"
                break
print(ans)