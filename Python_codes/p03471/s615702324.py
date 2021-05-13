n,yen = map(int,input().split())
isOK = False
for x in range(yen//10000+1):
    for y in range(yen//5000+1):
        if (n - x - y) >= 0:
            if yen == 10000 * x + 5000 * y + 1000 * (n - x - y):
                isOK = True
                break
    else:
        continue
    break
if isOK:
    print(x,y,n-x-y)
else:
    print(-1,-1,-1)