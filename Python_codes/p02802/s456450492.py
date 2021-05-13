n, m = map(int, input().split())
flg = [0]*n
ac = 0
pe = [0]*n

for i in range(m):
    p, s = input().split()
    if flg[int(p)-1] == 0:
        if s == "WA":
            pe[int(p)-1] += 1
        else:
            flg[int(p)-1] = 1
            ac += 1
spe = 0
for i in range(n):
    if flg[i] == 1:
        spe += pe[i]

print(ac, spe)
