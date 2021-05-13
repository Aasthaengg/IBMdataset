a, b, c, d, e, f = map(int, input().split())
tmp = {}

for i in range(31):
    for j in range(31):
        for k in range(101):
            for l in range(101):
                w = (100*a)*i + (100*b)*j
                s = c*k + d*l
                if w == 0:
                    break
                if w+s > f:
                    break
                else:
                    if w/100 * e >= s:
                        density = 100*s/(w+s)
                        tmp[w, s] = density

mxv = max(tmp, key=tmp.get)
print(mxv[0]+mxv[1], mxv[1])