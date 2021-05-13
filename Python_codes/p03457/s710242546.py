n = int(input())
TXY = []
tc, xc, yc = 0, 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    d = abs(x-xc)+abs(y-yc)
    if d > t-tc or (t-tc-d)%2 == 1:
        print('No')
        exit()
    else:
        tc, xc, yc = t, x, y
else:
    print('Yes')
