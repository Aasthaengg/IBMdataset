from collections import deque
h,w = map(int,input().split())
s = [0]*(h+2)
s[0]  = ["#"]*(w+2)
s[-1] = ["#"]*(w+2)
for i in range(h):
    s[i+1] = ["#"] + list(input()) + ["#"]
ans = 1
for i in range(h+2):
    for j in range(w+2):
        if s[i][j] != ".":
            pass
        else:
            xs,ys = j,i
            qx = deque([])
            qx.append(xs)
            qy = deque([])
            qy.append(ys)
            reach = [[0 for _1 in range(w+2)] for _2 in range(h+2)]
            reach[ys][xs] = 1
            while qx:
                x = qx.popleft()
                y = qy.popleft()

                if s[y-1][x] == "." and reach[y-1][x] == 0:
                    qx.append(x)
                    qy.append(y-1)
                    reach[y-1][x] = reach[y][x] + 1
                if s[y+1][x] == "." and reach[y+1][x] == 0:
                    qx.append(x)
                    qy.append(y+1)
                    reach[y+1][x] = reach[y][x] + 1
                if s[y][x-1] == "." and reach[y][x-1] == 0:
                    qx.append(x-1)
                    qy.append(y)
                    reach[y][x-1] = reach[y][x] + 1
                if s[y][x+1] == "." and reach[y][x+1] == 0:
                    qx.append(x+1)
                    qy.append(y)
                    reach[y][x+1] = reach[y][x] + 1
            m = 1
            for k in range(h+2):
                m = max(m,max(reach[k][:])-1)
            ans = max(ans,m)
print(ans)