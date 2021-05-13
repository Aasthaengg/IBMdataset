n,m,x = map(int,input().split())
books = list(list(map(int,input().split())) for i in range(n))
mon_lis = []
for i in range(2**n):
    mon = 0
    exp = [0]*m
    check=[0]*m
    for j in range(n):
        if (i >> j) & 1:
            mon += books[j][0]
            for k in range(m):
                exp[k] += books[j][k+1]
    for k in range(m):
        if exp[k] >= x:
            check[k] = 1
    if not 0 in check:
        mon_lis.append(mon)
if not mon_lis:
    print(-1)
else:
    print(min(mon_lis))