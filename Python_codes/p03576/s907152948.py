n,k=map(int,input().split())
xy=[list(map(int,input().split())) for _ in range(n)]
x=[xy[i][0] for i in range(n)]
y=[xy[i][1] for i in range(n)]
res = 10**20
for i in range(n):
    xl = xy[i][0]
    for j in range(n):
        xr = xy[j][0]
        if xr<xl:continue
        for p in range(n):
            yl = xy[p][1]
            for q in range(n):
                yr = xy[q][1]
                if yr<yl:continue
                tres = 0
                for sxy in xy:
                    if sxy[0] >= xl and sxy[0] <= xr and sxy[1] >= yl and sxy[1] <= yr:
                        tres += 1
                if tres >= k:
                    res = min(res,(xr-xl)*(yr-yl))
print(res)