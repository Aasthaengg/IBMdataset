h,w = map(int,input().split())
maze =["."*(w+2)] + [ "." + input() + "." for i in range(h) ] + ["."*(w+2)]
ans = []

for i in range(1,h+1):
    temp = ""
    for j in range(1,w+1):
        cnt = 0
        if maze[i][j] == "#":
            temp += "#"
        else:
            for y in range(-1,2,1):
                for x in range(-1,2,1):
                    if maze[i+y][j+x] == "#":
                        cnt += 1
            temp += str(cnt)
    ans += [temp]
for i in range(h):
    print(*ans[i],sep="")