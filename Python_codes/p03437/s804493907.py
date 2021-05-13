x,y = map(int,input().split())
r = 2
while 1:
    if x%y != 0:
        print(x)
        break
    elif x > 10**18:
        print(-1)
        break
    else:
        x *= r
        r += 1