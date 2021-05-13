N = int(input())
t = 0
x = 0
y = 0

for i in range(N):
    tt, xx, yy = map(int,input().split())
    if tt-t>=abs(xx-x)+abs(yy-y) and ((tt-t)-(abs(xx-x)+abs(yy-y)))%2==0:
        t = tt
        x = xx
        y = yy
    else:
        print('No')
        exit()
print('Yes')
