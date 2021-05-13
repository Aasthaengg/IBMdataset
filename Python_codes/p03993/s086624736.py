n = int(input())
dat = list(map(int, input().split()))
d = dict()
res = 0
for i in range(n):
    d[i+1] = dat[i]
    if d.get(dat[i], -1) == (i + 1):
        res += 1
print(res)