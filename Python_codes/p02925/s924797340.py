n = int(input())
e = [[] for _ in range(n * n)]
co = [0] * (n * n)
for i in range(n):
    a = [int(i)-1 for i in input().split()]
    for j in range(n - 2):
        aa, bb = min(i, a[j]), max(i, a[j])
        cc, dd = min(i, a[j+1]), max(i, a[j+1])
        e[aa * n + bb].append(cc * n + dd)
        co[cc * n + dd] += 1

x = []
for i in range(n * n):
    if co[i] == 0:
        x.append(i)

ans = 0
while x:
    y = []
    for i in x:
        for j in e[i]:
            co[j] -= 1
            if co[j] == 0:
                y.append(j)
    x = y
    ans += 1
if max(co) > 0:
    print(-1)
else:
    print(ans)
