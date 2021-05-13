a,b,c,d,e,f = map(int, input().split())

anum = f // (100*a)
bnum = f // (100*b)

cp = 0
for ca in range(anum+1):
    for cb in range(bnum+1):
        water = (a*ca + b*cb)*100
        if water > f:
            continue
        cnum = e * (a*ca+b*cb) // c
        dnum = e * (a*ca+b*cb) // d
        for cc in range(cnum+1):
            for cd in range(dnum+1):
                sugar = c*cc + d*cd
                # print(ca, cb, cc, cd, water, sugar)
                if water + sugar <= 0 or water + sugar > f or sugar > e * (a*ca+b*cb):
                    continue
                p = 100 * sugar / (water + sugar)
                if p >= cp:
                    cp = p
                    ans = [str(water + sugar), str(sugar)]
print(' '.join(ans))

