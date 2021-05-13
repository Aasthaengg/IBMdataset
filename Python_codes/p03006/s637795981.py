#各操作でコストゼロになるボールは一意
n = int(input())
x = []
y = []
for i in range(n):
    xi,yi =map(int, input().split( ))
    x.append(xi)
    y.append(yi)

cnt = {}

for i in range(n):
    for j in range(i):
        d1 = x[i]-x[j]
        d2 = y[i]-y[j]
        if (d1,d2) in cnt:
            cnt[(d1,d2)] += 1
        else:
            cnt[(d1,d2)] = 1
        if (-d1,-d2) in cnt:#こっちもいる
            cnt[(-d1,-d2)] += 1
        else:
            cnt[(-d1,-d2)] = 1

tmp = 0

for k in cnt:
    tmp = max(tmp, cnt[k])

print(n-tmp)