n = int(input())
dat = map(int, input().split())
dat = list(dat)
buf = [0] * 100100
buf[0] = 3
res = 1
M = (10**9 + 7)
for i in range(n):
    x = dat[i]
    res *= buf[x]
    res %= M
    buf[x] -= 1
    buf[x+1] += 1
print(res)

