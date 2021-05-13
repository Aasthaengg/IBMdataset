h , w = map(int,input().split())
s = [input() for i in range(h)]
coulef = [[0 for i in range(w)] for j in range(h)]
courig = [[0 for i in range(w)] for j in range(h)]
coudow = [[0 for i in range(w)] for j in range(h)]
couup = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
    cou = 0
    for j in range(w):
        if s[i][j] == ".":
            cou += 1
            courig[i][j] = cou
        elif s[i][j] == "#":
            cou = 0
for i in range(h):
    cou = 0
    for j in reversed(range(w)):
        if s[i][j] == ".":
            cou += 1
            coulef[i][j] = cou
        elif s[i][j] == "#":
            cou = 0
for i in range(w):
    cou = 0
    for j in range(h):
        if s[j][i] == ".":
            cou += 1
            coudow[j][i] = cou
        elif s[j][i] == "#":
            cou = 0
for i in range(w):
    cou = 0
    for j in reversed(range(h)):
        if s[j][i] == ".":
            cou += 1
            couup[j][i] = cou
        elif s[j][i] == "#":
            cou = 0

ans = 0
for i in range(h):
    for j in range(w):
        now = couup[i][j]+coudow[i][j]+coulef[i][j]+courig[i][j]
        ans = max(ans,now-3)
print(ans)