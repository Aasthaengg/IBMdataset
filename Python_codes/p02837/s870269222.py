n = int(input())
v = [[tuple(map(int, input().split()))for i in range(int(input()))]
     for i in range(n)]

ans = 0
for i in range(2**n):
    f = [0] * n
    xy = []
    for j in range(n):
        if (i >> j) & 1:
            f[j] = 1
            xy.append(v[j])
    flag = True
    for xyi in xy:
        for x, y in xyi:
            #print(f,x,y,bin(i))
            if (i>>(x-1))&1 != y:
                flag = False
                break
    if flag:
        ans = max(ans, len(xy))
print(ans)
