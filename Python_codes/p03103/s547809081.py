n,m = map(int,input().split())
ab = sorted([list(map(int,input().split())) for i in range(n)])
shop,cost,rest=0,0,m
while True:
    if ab[shop][1]<rest:
        cost += ab[shop][1]*ab[shop][0]
        rest -= ab[shop][1]
        shop+=1
    else:
        cost+=ab[shop][0]*rest
        break
print(cost)