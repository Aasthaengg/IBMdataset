import collections

h,w = map(int,input().split())
field = [["#"] + list(str(input())) + ["#"] for i in range(h)]

field.append(["#"]*(w+2))
field.insert(0,["#"]*(w+2))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def f():
    global ans
    s = q.popleft()
    y,x = s[0],s[1]
    for i in range(4):
        newy = y+dy[i]
        newx = x+dx[i]
        if field[newy][newx] == "." and memo[newy][newx] == "#": 
            q.append((newy,newx))
            memo[newy][newx] = memo[y][x] + 1
            ans = max(ans,memo[y][x] + 1)

ans = 0
for i in range(1,h+1):
    for j in range(1,w+1):
        if field[i][j] == "#":
            continue
        q = collections.deque()
        q.append((i,j))
        memo = [["#"]*(w+2) for i in range(h+2)]
        memo[i][j] = 0
        while q:
            f()

print(ans)
