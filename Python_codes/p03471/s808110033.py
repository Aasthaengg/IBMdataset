import sys

N, Y = map(int,input().split())

x = Y // 10000

for i in range(x+1):
    y = (Y - i*10000) // 5000
    for j in range(y+1):
        zan = Y - i*10000 - j*5000
        if zan < 0:
            continue
        else:
            z = zan//1000
            if (zan % 1000 == 0) and (N==i+j+z):
                print(i,j,z)
                sys.exit()
print(-1,-1,-1)
