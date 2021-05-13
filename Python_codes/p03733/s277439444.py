n, t = map(int,input().split())
dat = list(map(int, input().split()))
l = dat[0]
lt = dat[0]
res = 0
deteta = 0
for i in range(n):
    deteta = min(t,  dat[i] - lt)
    res += deteta
    l = dat[i] + t
    lt = dat[i]
print(t + res)