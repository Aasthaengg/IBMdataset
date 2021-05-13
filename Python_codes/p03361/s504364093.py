import sys

h, w = map(int, input().split())
p = []
for i in range(h):
    p.append(input())

ans = "Yes"
for i in range(h):
    for j in range(w):
        if p[i][j] != "#":
            continue
        _ = False
        # x(j):-1
        if j-1 >= 0 and p[i][j-1] == "#":
            _ = True
        # x:+1
        if j+1 < w and p[i][j+1] == "#":
            _ = True
        # y(i):-1
        if i-1 >= 0 and p[i-1][j] == "#":
            _ = True
        # y:+1
        if i+1 < h and p[i+1][j] == "#":
            _ = True
        if _ is False:
            ans = "No"
            print(ans)
            sys.exit()

print(ans)
