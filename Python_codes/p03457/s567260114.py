n = int(input())
tc = 0
xc, yc = 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    d = abs(x-xc)+abs(y-yc)
    if d > t-tc:
        print('No')
        exit()
    else:
        if (t-tc-d)%2 != 0:
            print('No')
            exit()
    xc, yc, tc = x, y, t
else:
    print('Yes')
