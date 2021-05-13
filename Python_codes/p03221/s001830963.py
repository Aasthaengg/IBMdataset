n,m = map(int,input().split())
py = [list(map(int,input().split())) for i in range(m)]
c = [0]*n
sort_py = sorted(py,key=lambda x:x[1])
ans = dict()
for p,y in sort_py:
    c[p-1] += 1
    ans[p,y] = str(p).zfill(6)+str(c[p-1]).zfill(6)

for p,y in py:
    print(ans[p,y])