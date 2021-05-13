a,b,m = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
xyc = [list(map(int, input().split())) for i in range(m)]
ans = min(al)+min(bl)
for l in xyc:
    p = al[l[0]-1] + bl[l[1]-1] -l[2]
    ans = min(ans,p)
print(ans)