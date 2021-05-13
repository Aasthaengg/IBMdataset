h,w = map(int,input().split())
l = [['*']*(w+2)]
for i in range(h):
    l.append(['*']+list(input())+['*'])
l.append(['*']*(w+2))


for i in range(1,h+1):
    s = ''
    for j in range(1,w+1):
        directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        alist = [(i+dir[0],j+dir[1]) for dir in directions]
        cnt = 0
        for a in alist:
            if l[a[0]][a[1]] == '#':
                cnt += 1
        if l[i][j] == '#':
            s += '#'
        else:
            s += str(cnt)
    print(s)
