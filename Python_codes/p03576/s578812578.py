N,K = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(N)]
xy.sort()
ans = 10**20
for l in range(N):
    for r in range(l,N,1):
        tmp=[]
        for i in range(l,r+1,1):
            tmp.append(xy[i][1])
        tmp.sort()
        for d in range(0,len(tmp)-K+1,1):
            ans = min(ans,(tmp[d+K-1]-tmp[d])*(xy[r][0]-xy[l][0]))

print(ans)