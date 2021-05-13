r,d,x = map(int,raw_input().split())
xi = x
nxi = 0
for i in range(10):
    nxi = xi*r -d
    print nxi
    xi = nxi