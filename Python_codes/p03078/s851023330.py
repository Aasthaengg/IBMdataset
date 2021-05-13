xx, yy, zz, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a.sort(reverse=1)
b.sort(reverse=1)
c.sort(reverse=1)
ans = []

for x in range(min(xx, k)):
    for y in range(min(yy, k // (x + 1))):
        for z in range(min(zz, k // ((x + 1) * (y + 1)))):
            ans.append(a[x] + b[y] + c[z])
ans.sort(reverse=1)

for i in range(k):
    print(ans[i])
