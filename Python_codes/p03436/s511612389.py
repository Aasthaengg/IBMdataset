h,w = map(int,input().split())
m = [list(map((lambda x: 0 if x == '#' else 1),list(input()))) for i in range(h)]
ret = sum(list(map(sum,m)))

q = [[0,0,0]]
m[0][0] = 0
while len(q)!=0:
    qtop = q.pop(0)
    x = qtop[0]
    y = qtop[1]
    d = qtop[2]
    if x == h-1 and y == w-1:
        print(ret-d-1)
        break
    if 0 < x and m[x-1][y] == 1:
        m[x-1][y] = 0
        q.append([x-1,y,d+1])
    if h-1 > x and m[x+1][y] == 1:
        m[x+1][y] = 0
        q.append([x+1,y,d+1])
    if 0 < y and m[x][y-1] == 1:
        m[x][y-1] = 0
        q.append([x,y-1,d+1])
    if w-1 > y and m[x][y+1] == 1:
        m[x][y+1] = 0
        q.append([x,y+1,d+1])
else:
    print(-1)
