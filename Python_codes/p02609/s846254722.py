n = int(input())
x = input()

c = x.count('1')
cp = c+1
cn = c-1

rp = [0] * n
if cp > 1:
    rp[0] = 1
rn = [0] * n
if cn > 1:
    rn[0] = 1
for i in range(1, n):
    rp[i] = (rp[i-1] * 2) % cp
    if cn > 0:
        rn[i] = (rn[i-1] * 2) % cn

xp = 0
xn = 0
for i in range(n):
    xx = x[i]
    if xx == '1':
        xp = (xp + rp[n-i-1]) % cp
        if cn > 0:
            xn = (xn + rn[n-i-1]) % cn

for i in range(n):
    o = 1
    if x[i] == '1':
        if cn == 0:
            print(0)
            continue
        xx = (xn-rn[n-i-1]) % cn
    else:
        xx = (xp+rp[n-i-1]) % cp
    while xx > 0:
        cc = bin(xx)[2:].count('1')
        xx = xx % cc
        o += 1
    print(o)
