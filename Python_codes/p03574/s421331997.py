h, w = map(int, input().split())
s = []
s.append("."*(w+2))
for _ in range(h):
    s.append("."+input()+".")
s.append("."*(w+2))
for i in range(1, h+1):
    ans = ""
    for j in range(1, w+1):
        if s[i][j] == ".":
            ans += str([s[i-1][j-1], s[i-1][j], s[i-1][j+1], s[i][j-1], s[i][j+1], s[i+1][j-1], s[i+1][j], s[i+1][j+1]].count("#"))
        else:
            ans += "#"
    print(ans)