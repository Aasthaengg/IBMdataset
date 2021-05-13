n = int(input())
dat = list(map(int, input().split()))
p = dat[0]
res = 0
for i in range(1, len(dat)):
    if p == dat[i]:
        dat[i] = "x"
        p = "x"
        res += 1
    else:
        p = dat[i]
print(res)
