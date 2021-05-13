n = int(input())
dat = list(map(int, input().split()))
dat.sort()
x = dat[-1]
xx = x / 2
dat = dat[:-1]
mindiff = 999999999999999999999999999
minnum = None
for i in range(n-1):
    if abs(xx-dat[i]) < mindiff:
        mindiff = abs(xx-dat[i])
        minnum = dat[i]
print(x, minnum)