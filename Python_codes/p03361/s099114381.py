h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]
black = []
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            black.append([i,j])
for x,y in black:
    flag = False
    for a,b in [(0,1), (1,0), (0,-1), (-1,0)]:
        if [x+a, y+b] in black: flag = True
    if not flag:
        print("No")
        exit()
print("Yes")