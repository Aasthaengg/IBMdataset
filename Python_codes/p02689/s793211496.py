n,m = map(int,input().split())
h = list(map(int,input().split()))
ab = [list(map(int,input().split())) for i in range(m)]
hill = [i for i in range(1,n+1)]
for i in range(len(ab)):
    a,b = ab[i][0],ab[i][1]
    if h[a-1] > h[b-1]:
        hill[b-1] = 0
    elif h[a-1] < h[b-1]:
        hill[a-1] = 0
    elif h[a-1] == h[b-1]:
        hill[a-1] = 0
        hill[b-1] = 0

print(n-hill.count(0))
