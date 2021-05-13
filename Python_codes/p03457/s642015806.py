N = int(input())
t = 0
x = 0
y = 0
for ti, xi, yi in [map(int, input().split(' ')) for n in range(N)]:
    if not (abs(xi-x)+abs(yi-y) <= ti-t and ti%2 == (xi+yi)%2):
        print('No')
        exit()
    else:
        t = ti
        x = xi
        y = yi
print('Yes')