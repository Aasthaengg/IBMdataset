import sys
input = sys.stdin.readline

x, y = map(int,input().split())

if x % y == 0:
    print(-1)
else:
    for i in range(x,1000000000000000000,x):
        if i % y !=0:
            print(i)
            break