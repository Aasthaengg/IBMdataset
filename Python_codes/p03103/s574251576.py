N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]
AB=sorted(AB)
cost=0
x=0
for ab in AB:
    if x+ab[1]<M:
        cost+=ab[0]*ab[1]
        x+=ab[1]
    else:
        cost+=ab[0]*(M-x)
        break
print(cost)
