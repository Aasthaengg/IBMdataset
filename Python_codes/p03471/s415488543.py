import sys
a,b = map(int,input().split())
for x in range(a+1):
    for y in range(a+1):
            if 10000*x + 5000*y + 1000*(a-x-y) > b:
                if a-x-y >= 0:
                    continue
            if 10000*x + 5000*y + 1000*(a-x-y) == b:
                if a-x-y >= 0:
                    print(x,y,a-x-y)
                    sys.exit()
print(-1,-1,-1)