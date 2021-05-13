a, b, c, d, e, f = map(int,input().split())
wa = []
for ia in range(30):
    for ib in range(30):
        if 100*(ia*a+ib*b) <= f and not 100*(ia*a+ib*b) in wa:
            wa.append(ia*a+ib*b)

msu = [0 for i in range(len(wa))]
mc = -0.01
mci = -1
for i,w in enumerate(wa):
    for ic in range(1501):
        for id in range(1501):
            if ic*c+id*d > e*w:
                break
            if ic*c+id*d+w*100 > f:
                break
            if msu[i] < ic*c+id*d:
                msu[i] = ic*c+id*d
                if mc < (ic*c+id*d)/(ic*c+id*d+w*100):
                    mc = (ic*c+id*d)/(ic*c+id*d+w*100)
                    mci = i

print(wa[mci]*100+msu[mci],msu[mci])
