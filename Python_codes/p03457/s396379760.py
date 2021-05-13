N = int(input())
moromoro = [list(map(int,input().split())) for _ in range(N)]
moromoro.sort()

t,x,y = 0,0,0
for i in range(N):
    time = moromoro[i][0] - t
    dx = abs(moromoro[i][1] - x)
    dy = abs(moromoro[i][2] - y)
    if  dx + dy > time:
        print('No')
        exit()
    if (time - dx - dy) % 2 == 1:
        print('No')
        exit()
    t = moromoro[i][0]
    x = moromoro[i][1]
    y = moromoro[i][2]
print('Yes')


