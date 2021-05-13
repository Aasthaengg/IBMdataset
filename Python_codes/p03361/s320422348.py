h,w = map(int,input().split())
g = [[0]*(w+2)]+[[0]+[(i == "#")*1 for i in list(input())]+[0] for _ in range(h)]+[[0]*(w+2)]

for i in range(1,h+1):
    for j in range(1,w+1):
        t = 0
        if g[i][j] == 0:
            continue
        if g[i-1][j] == 1:
            t += 1
        if g[i+1][j] == 1:
            t += 1
        if g[i][j-1] == 1:
            t += 1
        if g[i][j+1] == 1:
            t += 1
        if t == 0:
            print("No")
            quit()

print("Yes")
