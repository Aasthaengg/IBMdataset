h, w = map(int, input().split())

wall = ["." * (w + 2)]
s = wall + ["." + input() + "." for _ in range(h)] + wall

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == ".":
            t = s[i-1][j-1:j+2] + s[i][j-1:j+2] + s[i+1][j-1:j+2]
            s[i] = s[i][:j] + str(t.count("#")) + s[i][j+1:]
    else:
        print(s[i][1:-1])